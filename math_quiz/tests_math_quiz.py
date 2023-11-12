import unittest
from math_quiz import rand_int, rand_op, rand_prob


class TestMathGame(unittest.TestCase):

    def test_rand_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = rand_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_rand_op(self):
        # Test if the function returns one of the expected operators
        for _ in range(1000):
            operator = rand_op()
            self.assertTrue(operator in ['+', '-', '*'])

        
    def test_rand_prob(self):
            test_cases = [(5, 2, '+', '5 + 2', 7), (6, 1, '-', '6 - 1', 5),
                          (9, 2, '*', '9 * 2', 18)]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = rand_prob(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
