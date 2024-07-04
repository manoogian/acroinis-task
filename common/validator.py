class Validator:
    valid_operation = ['+', '-', '/', '*']
    required_fields = ['identifier', 'operation', 'left_operand', 'right_operand']

    def check_operation(self, operation):
        if operation not in self.valid_operation:
            raise ValueError("Invalid Operation.")

    def check_identifier(self, identifier, allowed_clients):
        if identifier not in allowed_clients:
            raise ValueError("Unknown client identifier.")

    def check_required_fields(self, data):
        if not all(field in data for field in self.required_fields):
            raise ValueError("Missing required fields.")

    def check_integer(self, number):
        if not isinstance(number, int):
            raise ValueError("Numbers must be integers.")

    def check_positive(self, number):
        if number <= 0:
            raise ValueError("Numbers must be positive integers.")

    def check_number(self, value):
        if not value.isdigit():
            raise ValueError("Input must be a positive integer.")

    def ckeck_result_condition(self, result):
        if result > 100:
            raise ValueError("Result more than 100")
