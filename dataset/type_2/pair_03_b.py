def has_no_divisors(candidate):
    if candidate < 2:
        return False
    for test_value in range(2, int(candidate ** 0.5) + 1):
        if candidate % test_value == 0:
            return False
    return True


print(has_no_divisors(31))
