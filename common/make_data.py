import json


class DataParser:

    def create_client_json(self, client, left_operand, right_operand, operation):
        data = {
            'identifier': client,
            'left_operand': left_operand,
            'right_operand': right_operand,
            'operation': operation
        }
        return json.dumps(data)
