def power(base, exponent):
    result = 1

    for _ in range(exponent):
        result *= base

    return result  # 81

def power_of_two(n):
    result = 1
    for _ in range(n):
        result *= 2
    return result

def is_perfect_square(n):
    if n < 0:
        return False
    root = int(n ** 0.5)
    return power(root, 2) == n

def powers_sequence(base, count):
    result = []
    for exp in range(count):
        result.append(power(base, exp))
    return result

print(power(3, 4))
print(power(2, 10))
print(power_of_two(8))
print(is_perfect_square(49))
print(is_perfect_square(50))
print(powers_sequence(2, 8))
