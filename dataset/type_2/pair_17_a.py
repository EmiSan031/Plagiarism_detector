def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a

def lcm(a, b):
    common = gcd(a, b)
    return (a * b) // common

def are_coprime(a, b):
    return gcd(a, b) == 1

def divisor_report(a, b):
    if a <= 0 or b <= 0:
        print("Both numbers must be positive integers.")
        return
    common = gcd(a, b)
    multiple = lcm(a, b)
    coprime = are_coprime(a, b)
    print(f"Number A        : {a}")
    print(f"Number B        : {b}")
    print(f"GCD({a}, {b})       : {common}")
    print(f"LCM({a}, {b})       : {multiple}")
    if coprime:
        print(f"Coprime         : Yes (GCD = 1)")
    else:
        print(f"Coprime         : No  (GCD = {common})")
    print(f"A divisible by GCD: {a % common == 0}")
    print(f"B divisible by GCD: {b % common == 0}")
    print(f"GCD * LCM       : {common * multiple} (should equal {a * b})")

divisor_report(84, 30)
