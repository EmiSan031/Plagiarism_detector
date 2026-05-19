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

def candidates_up_to(ceiling):
    found = []
    for num in range(2, ceiling + 1):
        if has_no_divisors(num):
            found.append(num)
    return found

def following_prime(num):
    probe = num + 1
    while not has_no_divisors(probe):
        probe += 1
    return probe

def candidate_report(num):
    outcome = has_no_divisors(num)
    print(f"Number          : {num}")
    print(f"Is prime        : {outcome}")
    found = candidates_up_to(num)
    print(f"Primes up to {num}: {found}")
    print(f"Count           : {len(found)}")
    if outcome:
        print(f"Next prime after {num}: {following_prime(num)}")
    else:
        print(f"Nearest prime   : {following_prime(num - 1)}")

candidate_report(29)
