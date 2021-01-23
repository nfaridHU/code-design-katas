def prime_factors(number):
    prime_numbers = [2, 3, 5]
    factors = []

    for p_number in prime_numbers:
        while number % p_number == 0:
            factors.append(p_number)
            number = number // p_number

    return factors
