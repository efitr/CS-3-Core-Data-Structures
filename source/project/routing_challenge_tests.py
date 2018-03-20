from routing_challenge import divide_format, cost_of_calling_a_number_iterative
import unittest

class RoutingTest(unittest.TestCase):
    
    def test_divide_format(self):
        assert divide_format("+86153,0.84") is "+86153" and "0.84"
        assert divide_format("+1426793,0.09") is "+1426793" and "0.09"

    #must solve because the function expects 2 but gets 1
    def test_divide_format_without_price(self):
        assert divide_format("+86153") is None
    
    def test_divide_format_without_route(self):
        assert divide_format("0.043") is None

    def test_cost_of_calling_a_number_iterative(self):
        assert cost_of_calling_a_number_iterative("+86153,0.84", "+8615334567") is 0.84

if __name__ == '__main__':
    unittest.main()