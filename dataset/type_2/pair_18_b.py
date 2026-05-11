def repeated_multiply(value, times):
    product = 1
    for _ in range(times):
        product *= value
    return product


print(repeated_multiply(2, 5))
