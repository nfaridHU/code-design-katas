def fibonacci(position):
    if position in [0, 1]:
        return position

    previous, current = 0, 1
    for p in range(2, position + 1):
        previous, current = current, current + previous

    return current
