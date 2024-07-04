class ComputationRequest:
    def __init__(self, left_operand: int, right_operand: int, operation):
        self.lhs = left_operand
        self.rhs = right_operand
        self.operation = operation
