

class Year:

    def __init__(self, physical_value):
        """

        :param physical_value: year
        """
        self.physical_value = physical_value

    def is_leap_year(self):
        """
        :return: bool - returns True if year is a leap year
        """
        return self.is_divisible_by(400) or not self.is_divisible_by(100) and self.is_divisible_by(4)

    def is_divisible_by(self, x):
        return self.physical_value % x == 0
