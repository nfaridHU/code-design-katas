import unittest

from prime_factors import prime_factors


class PrimeFactorShould(unittest.TestCase):

    ## Deprecated due to a superior test
    # def test_return_a_list(self):
    #     self.assertEqual(list, type(prime_factors(2)))

    def test_return_factors_of_2(self):
        self.assertEqual([2], prime_factors(2))

    def test_return_factors_of_3(self):
        self.assertEqual([3], prime_factors(3))

    def test_return_factors_of_4(self):
        self.assertEqual([2, 2], prime_factors(4))

    def test_return_factors_of_6(self):
        self.assertEqual([2, 3], prime_factors(6))

    def test_return_factors_of_9(self):
        self.assertEqual([3, 3], prime_factors(9))

    def test_return_factors_of_12(self):
        self.assertEqual([2, 2, 3], prime_factors(12))

    def test_return_factors_of_15(self):
        self.assertEqual([2, 3, 3], prime_factors(18))




if __name__ == '__main__':
    unittest.main()
