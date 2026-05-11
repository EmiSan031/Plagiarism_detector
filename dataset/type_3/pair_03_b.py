def has_no_divisors(candidate):
    if candidate < 2:
        return False
    if candidate == 2:
        return True
    if candidate % 2 == 0:
        return False
    for test_value in range(3, int(candidate ** 0.5) + 1):
        if candidate % test_value == 0:
            return False
    return True


print(has_no_divisors(29))
