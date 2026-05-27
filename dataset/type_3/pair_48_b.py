def euclid(x, y):
    x, y = abs(x), abs(y)
    while y != 0:
        x, y = y, x % y
    return x

def common_multiple(x, y):
    return (abs(x) * abs(y)) // euclid(x, y)

def shared_divisor(values):
    if len(values) == 0:
        return None
    outcome = values[0]
    for val in values[1:]:
        outcome = euclid(outcome, val)
    return outcome

def shared_multiple_all(values):
    if len(values) == 0:
        return None
    outcome = values[0]
    for val in values[1:]:
        outcome = common_multiple(outcome, val)
    return outcome

def are_coprime_pair(x, y):
    return euclid(x, y) == 1

def divisor_report(values):
    if len(values) == 0:
        print("Empty list provided.")
        return None, None
    divisor = shared_divisor(values)
    multiple = shared_multiple_all(values)
    coprime_pairs = 0
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if are_coprime_pair(values[i], values[j]):
                coprime_pairs += 1
    print(f"Values          : {values}")
    print(f"Count           : {len(values)}")
    print(f"GCD of all      : {divisor}")
    print(f"LCM of all      : {multiple}")
    print(f"All divisible   : {all(v % divisor == 0 for v in values)}")
    print(f"Coprime pairs   : {coprime_pairs}")
    return divisor, multiple

divisor_report([12, 18, 24, 36])
