class Calculator:
    def __init__(self):
        self.action_dict = {
            "+": self.sum,
            "-": self.subtract,
            "*": self.multiple,
            "/": self.division
        }

    def sum(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def division(self, a, b):
        return a / b

    def multiple(self, a, b):
        return a * b

    def calculate(self, a, b, operation):
        return self.action_dict[operation](a, b)

