import unittest

from fizz_buzz import fizzbuzz


class FizzBuzzShould(unittest.TestCase):
    def test_return_1_when_1_is_given(self):
        self.assertEqual("1", fizzbuzz(1))

    def test_return_2_when_2_is_given(self):
        self.assertEqual("2", fizzbuzz(2))

    def test_return_fizz_when_3_is_given(self):
        self.assertEqual("fizz", fizzbuzz(3))

    def test_return_fizz_when_multiples_of_3_is_given(self):
        for m in range(3, 15, 3):
            self.assertEqual("fizz", fizzbuzz(m))

    def test_return_buzz_when_5_is_given(self):
        self.assertEqual("buzz", fizzbuzz(5))

    def test_return_buzz_when_multiples_of_5_is_given(self):
        for m in range(5, 15, 5):
            self.assertEqual("buzz", fizzbuzz(m))

    def test_return_fizzbuzz_when_multiples_of_3_and_5_is_given(self):
        for m in range(15, 115, 15):
            self.assertEqual("fizzbuzz", fizzbuzz(m))


if __name__ == '__main__':
    unittest.main()
