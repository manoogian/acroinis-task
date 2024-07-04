import os
import sys

if os.path.dirname(os.path.dirname((os.path.abspath(__file__)))) not in sys.path:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import client.client as cl
import client.computation_request as cr


class TestClient:

    def test_client_positive_numbers_negative_case(self):
        client = cl.Client(identifier="client1")

        request = cr.ComputationRequest(-10, 30, '+')
        response = client.execute_request(request)

        assert response == 'Error: Numbers must be positive integers.'

    def test_client_positive_numbers_positive_case(self):
        client = cl.Client(identifier="client1")

        request = cr.ComputationRequest(10, 30, '+')
        response = client.execute_request(request)

        assert response == "Result: 40"

    def test_client_large_sum(self):
        client = cl.Client(identifier="client1")

        request = cr.ComputationRequest(40, 70, '+')
        response = client.execute_request(request)

        assert response == "Error: Result more than 100"

    def test_simple_subtract(self):
        client = cl.Client(identifier="client1")

        request = cr.ComputationRequest(70, 50, '-')
        response = client.execute_request(request)

        assert response == "Result: 20"
