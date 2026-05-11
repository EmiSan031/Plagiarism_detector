def gcd(a, b):
    # Euclidean algorithm.
    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    return a


print(gcd(84, 30))
