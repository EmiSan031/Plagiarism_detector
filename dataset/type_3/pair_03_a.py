def is_prime(n):
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True

def primes_up_to(limit):
    primes = []
    for number in range(2, limit + 1):
        if is_prime(number):
            primes.append(number)
    return primes

def next_prime(n):
    candidate = n + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate

def prime_report(n):
    result = is_prime(n)
    print(f"Number          : {n}")
    print(f"Is prime        : {result}")
    primes = primes_up_to(n)
    print(f"Primes up to {n} : {primes}")
    print(f"Count           : {len(primes)}")
    if result:
        print(f"Next prime after {n}: {next_prime(n)}")
    else:
        print(f"Nearest prime   : {next_prime(n - 1)}")

prime_report(29)
