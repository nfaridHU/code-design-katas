import unittest

from fibonacci import fibonacci


class FibonacciShould(unittest.TestCase):

    def test_call(self):
        fibonacci(4)

    def test_return_0_when_0_is_given(self):
        self.assertEqual(0, fibonacci(0))

    def test_return_1_when_1_is_given(self):
        self.assertEqual(1, fibonacci(1))

    def test_n_returns_sum_of_previous_two_fibonacci(self):
        for i in range(2, 50):
            self.assertEqual(fibonacci(i-2) + fibonacci(i-1), fibonacci(i))
