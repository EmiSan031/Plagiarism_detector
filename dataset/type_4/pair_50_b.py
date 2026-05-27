def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def primes_up_to(limit):
    return sieve_of_eratosthenes(limit)

def prime_factors(n):
    factors = []
    for p in sieve_of_eratosthenes(int(n ** 0.5) + 1):
        while n % p == 0:
            factors.append(p)
            n //= p
    if n > 1:
        factors.append(n)
    return factors

def nth_prime(n):
    primes = sieve_of_eratosthenes(n * 15)
    return primes[n - 1]

print(primes_up_to(50))
print(prime_factors(360))
print(nth_prime(10))
