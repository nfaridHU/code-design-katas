import unittest

from leap_year import Year


def is_leap_year(physical_value):
    year = Year(physical_value)
    return year.is_leap_year()


class LeapYearShould(unittest.TestCase):

    def check_assertion(self, y, expected):
        year = Year(y)
        self.assertEqual(year.is_leap_year(), expected)
        del year

    def assert_if_leap_year(self, y):
        self.check_assertion(y, True)

    def assert_if_not_leap_year(self, y):
        self.check_assertion(y, False)

    def test_return_true_if_year_is_divisible_by_4(self):
        for y in range(4, 100, 4):
            self.assert_if_leap_year(y)

    def test_return_false_if_year_is_not_divisible_by_4(self):
        for y in range(1, 100):
            if y % 4:
                self.assert_if_not_leap_year(y)

    def test_return_false_if_year_is_divisible_by_100_and_not_by_400(self):
        for y in range(100, 1001, 100):
            if y % 400:
                self.assert_if_not_leap_year(y)

    def test_return_true_if_year_is_divisible_by_400(self):
        for y in range(400, 2001, 400):
            self.assert_if_leap_year(y)

    def test_return_false_on_typical_years(self):
        self.assert_if_not_leap_year(2001)
        self.assert_if_not_leap_year(1900)

    def test_return_true_on_leap_years(self):
        self.assert_if_leap_year(1996)
        self.assert_if_leap_year(2000)


if __name__ == '__main__':
    unittest.main()
