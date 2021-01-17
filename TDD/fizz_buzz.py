class FizzBuzzNumber(int):
    def __init__(self, input):
        self.input = input

    def is_multiple_of(self, number):
        return self.input % number == 0


def fizzbuzz(number):
    fizzbuzz_number = FizzBuzzNumber(number)
    if fizzbuzz_number.is_multiple_of(3) and fizzbuzz_number.is_multiple_of(5):
        return "fizzbuzz"
    if fizzbuzz_number.is_multiple_of(3):
        return "fizz"
    if fizzbuzz_number.is_multiple_of(5):
        return "buzz"

    return str(number)

# YAGNI -- You Aren't Gonna Need It - a principle of extreme programming 
