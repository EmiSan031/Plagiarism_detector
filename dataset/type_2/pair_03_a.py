def is_prime(n):
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True

def get_primes_in_range(start, end):
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes

def print_prime_report(start, end):
    print(f"Checking prime numbers between {start} and {end}:")
    print("-" * 40)
    primes = get_primes_in_range(start, end)
    for p in primes:
        print(f"  {p} -> PRIME")
    print("-" * 40)
    print(f"Total primes found: {len(primes)}")
    return primes

result = print_prime_report(2, 40)
print(f"Is 29 prime? {is_prime(29)}")
