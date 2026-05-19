def has_no_divisors(candidate):
    if candidate < 2:
        return False
    for test_value in range(2, int(candidate ** 0.5) + 1):
        if candidate % test_value == 0:
            return False
    return True

def collect_primes(lower, upper):
    found = []
    for num in range(lower, upper + 1):
        if has_no_divisors(num):
            found.append(num)
    return found

def show_prime_summary(lower, upper):
    print(f"Scanning for prime numbers from {lower} to {upper}:")
    print("-" * 40)
    found = collect_primes(lower, upper)
    for entry in found:
        print(f"  {entry} -> PRIME")
    print("-" * 40)
    print(f"Total prime numbers detected: {len(found)}")
    return found

outcome = show_prime_summary(2, 40)
print(f"Is 31 prime? {has_no_divisors(31)}")
