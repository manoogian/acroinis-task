import os
import sys

if os.path.dirname(os.path.dirname((os.path.abspath(__file__)))) not in sys.path:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import socket

from common.validator import Validator
from common.make_data import DataParser


class Client:
    def __init__(self, identifier, host='localhost', port=65432):
        self.identifier = identifier
        self.host = host
        self.port = port
        self.connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect.connect((self.host, self.port))
        self.user_input_validator = Validator()

    def execute_request(self, computation_request):

        data = DataParser().create_client_json(client=self.identifier,
                                               left_operand=computation_request.lhs,
                                               right_operand=computation_request.rhs,
                                               operation=computation_request.operation)

        self.connect.sendall(data.encode('utf-8'))

        return self.receive()


    def validate_operation(self, operation):
        self.user_input_validator.check_operation(operation)
        return operation

    def receive(self):
        response = self.connect.recv(1024).decode('utf-8')
        return response



