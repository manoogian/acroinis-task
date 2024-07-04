import os
import sys

if os.path.dirname(os.path.dirname((os.path.abspath(__file__)))) not in sys.path:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import socket
import json
import calc_engine as calc
from common.validator import Validator


class Server:
    def __init__(self, host='localhost', port=65432):
        self.host = host
        self.port = port
        self.allowed_identifiers = ["client1", "client2"]
        self.validate = Validator()
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_connection = None

    def server_start_listening(self):
        self.connection.bind((self.host, self.port))
        self.connection.listen()
        print(f"Server listening on {self.host}:{self.port}")

    def receive_data(self):
        self.socket_connection, addr = self.connection.accept()

        print(f"Connected by {addr}")
        data = self.socket_connection.recv(1024).decode('utf-8')
        return json.loads(data)

    def send_to_client(self, response):
        print(response)
        self.socket_connection.sendall(response.encode('utf-8'))

    def start_server(self):
        self.server_start_listening()

        while True:
            try:
                data_dict = self.receive_data()
                self.validate_data(data_dict)

                result = calc.Calculator().calculate(data_dict['left_operand'],
                                                     data_dict['right_operand'],
                                                     data_dict['operation'])
                self.validate.ckeck_result_condition(result)
                result = f"Result: {result}"
            except (json.JSONDecodeError, KeyError, ValueError) as e:
                result = f"Error: {e}"
                print(result)
                self.send_to_client(result)

            self.send_to_client(result)

    def validate_data(self, data):
        self.validate.check_required_fields(data)
        self.validate.check_identifier(data['identifier'], self.allowed_identifiers)
        self.validate.check_integer(data['left_operand'])
        self.validate.check_integer(data['right_operand'])
        self.validate.check_positive(data['left_operand'])
        self.validate.check_positive(data['right_operand'])


if __name__ == "__main__":
    server = Server()
    server.start_server()
