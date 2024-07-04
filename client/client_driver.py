from common.validator import Validator
from computation_request import ComputationRequest
from client import Client


class MyApp:
    def __init__(self, calculator_client):
        self.calculator_client = calculator_client
        self.input_validator = Validator()

    def validate_and_convert_operand(self, operand):
        self.input_validator.check_number(operand)
        value = int(operand)
        self.input_validator.check_integer(value)
        self.input_validator.check_positive(value)
        return value

    def create_request(self):
        lhs_input = input("Enter the first positive integer: ")
        rhs_input = input("Enter the second positive integer: ")
        operation_input = input("Choose one operation (*, /, +, -): ")

        lhs_value = self.validate_and_convert_operand(lhs_input)
        rhs_value = self.validate_and_convert_operand(rhs_input)

        return ComputationRequest(lhs_value, rhs_value, operation_input)

    def run(self):
        request = self.create_request()
        response = self.calculator_client.execute_request(request)
        print("Computation Response:", response)


if __name__ == "__main__":
    my_shiny_app = MyApp(Client(identifier="client1"))
    my_shiny_app.run()
