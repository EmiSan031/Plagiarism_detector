def common_divisor(first, second):
    while second != 0:
        rest = first % second
        first = second
        second = rest
    return first

def shared_multiple(first, second):
    shared = common_divisor(first, second)
    return (first * second) // shared

def mutually_prime(first, second):
    return common_divisor(first, second) == 1

def gcd_report(first, second):
    if first <= 0 or second <= 0:
        print("Both inputs must be positive integers.")
        return
    shared = common_divisor(first, second)
    multiple = shared_multiple(first, second)
    prime_check = mutually_prime(first, second)
    print(f"First number    : {first}")
    print(f"Second number   : {second}")
    print(f"GCD({first}, {second})      : {shared}")
    print(f"LCM({first}, {second})      : {multiple}")
    if prime_check:
        print(f"Mutually prime  : Yes (GCD = 1)")
    else:
        print(f"Mutually prime  : No  (GCD = {shared})")
    print(f"First / GCD     : {first % shared == 0}")
    print(f"Second / GCD    : {second % shared == 0}")
    print(f"GCD * LCM       : {shared * multiple} (should equal {first * second})")

gcd_report(96, 36)
