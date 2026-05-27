def proper_divisors(num):
    factors = []
    for candidate in range(1, num):
        if num % candidate == 0:
            factors.append(candidate)
    return factors

def classify_number(num):
    if num < 2:
        return "neither"
    factor_sum = sum(proper_divisors(num))
    if factor_sum == num:
        return "perfect"
    elif factor_sum > num:
        return "abundant"
    else:
        return "deficient"

def find_perfect(ceiling):
    if ceiling < 0:
        return []
    found = []
    for num in range(2, ceiling + 1):
        if classify_number(num) == "perfect":
            found.append(num)
    return found

def number_report(ceiling):
    if ceiling < 0:
        print(f"Invalid ceiling: {ceiling}")
        return []
    found = find_perfect(ceiling)
    print(f"Searching up to : {ceiling}")
    print(f"Perfect numbers : {found}")
    print(f"Count found     : {len(found)}")
    for num in found:
        factors = proper_divisors(num)
        print(f"  {num} -> factors: {factors} -> sum: {sum(factors)}")
    return found

number_report(500)
