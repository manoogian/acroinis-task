import os
import sys
import json
import asyncio

# Ensure the necessary directories are in sys.path
if os.path.dirname(os.path.dirname(os.path.abspath(__file__))) not in sys.path:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import calc_engine as calc
from common.validator import Validator

class Server:
    def __init__(self, host='localhost', port=65432):
        self.host = host
        self.port = port
        self.allowed_identifiers = ["client1", "client2"]
        self.validate = Validator()
        self.connection = None

    async def server_start_listening(self):
        self.connection = await asyncio.start_server(self.handle_client, self.host, self.port)
        addr = self.connection.sockets[0].getsockname()
        print(f"Server listening on {addr}")

    async def receive_data(self, reader):
        data = await reader.read(1024)
        message = data.decode('utf-8')
        return json.loads(message)

    async def send_to_client(self, writer, response):
        print(f"Sending to client: {response}")
        writer.write(response.encode('utf-8'))
        await writer.drain()

    async def handle_client(self, reader, writer):
        addr = writer.get_extra_info('peername')
        print(f"Connected by {addr}")

        try:
            data_dict = await self.receive_data(reader)
            self.validate_data(data_dict)

            result = calc.Calculator().calculate(data_dict['left_operand'],
                                                 data_dict['right_operand'],
                                                 data_dict['operation'])
            self.validate.ckeck_result_condition(result)
            response = f"Result: {result}"
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            response = f"Error: {e}"
            print(response)

        await self.send_to_client(writer, response)

        print("Closing the connection")
        writer.close()
        await writer.wait_closed()

    def validate_data(self, data):
        self.validate.check_required_fields(data)
        self.validate.check_identifier(data['identifier'], self.allowed_identifiers)
        self.validate.check_integer(data['left_operand'])
        self.validate.check_integer(data['right_operand'])
        self.validate.check_positive(data['left_operand'])
        self.validate.check_positive(data['right_operand'])

    async def start_server(self):
        await self.server_start_listening()
        async with self.connection:
            await self.connection.serve_forever()

if __name__ == "__main__":
    server = Server()
    asyncio.run(server.start_server())
