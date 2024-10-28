import unittest
from math_quiz import *


class TestMathGame(unittest.TestCase):

    def test_random_input(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_input(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        # Test if random operators generated are valid
        expected_operators = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random operators
            operator = random_operator()
            self.assertIn(operator, expected_operators)
        pass

    def test_operation(self):
        # Test if the operation function returns the correct result
        test_cases = [
                    (5, 3, '+', 8),
                    (5, 3, '-', 2),
                    (5, 3, '*', 15),
                    (6, 3, '/', 2),
                    (5, 0, '/', None)  # Assuming the function returns None for division by zero
                ]

        for a, b, op, expected in test_cases:
            with self.subTest(a=a, b=b, op=op, expected=expected):
                result = operation(a, b, op)
                self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
