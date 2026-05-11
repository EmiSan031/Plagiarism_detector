def is_prime(n):
    return n >= 2 and all(n % divisor != 0 for divisor in range(2, int(n ** 0.5) + 1))


print(is_prime(29))
