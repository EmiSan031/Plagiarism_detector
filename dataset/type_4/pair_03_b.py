def is_prime(n):
    return n >= 2 and all(
        n % divisor != 0 for divisor in range(2, int(n ** 0.5) + 1)
    )

def primes_up_to(limit):
    return [n for n in range(2, limit + 1) if is_prime(n)]

def count_primes(limit):
    return sum(1 for n in range(2, limit + 1) if is_prime(n))

def next_prime(n):
    return next(
        candidate for candidate in range(n + 1, n + 1000) if is_prime(candidate)
    )

print(is_prime(29))
print(primes_up_to(30))
print(count_primes(50))
print(next_prime(10))
