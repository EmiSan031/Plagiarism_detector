def repeated_multiply(value, times):
    if times < 0:
        return None
    product = 1
    counter = 0
    for _ in range(times):
        product *= value
        counter += 1
    print("multiplications:", counter)
    return product


print(repeated_multiply(3, 4))
