def power(base, exponent):
    return base ** exponent

def power_of_two(n):
    return 2 ** n

def is_perfect_square(n):
    if n < 0:
        return False
    return int(n ** 0.5) ** 2 == n

def powers_sequence(base, count):
    return [base ** exp for exp in range(count)]

print(power(3, 4))
print(power_of_two(8))
print(is_perfect_square(49))
print(is_perfect_square(50))
print(powers_sequence(2, 8))
