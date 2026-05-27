def num_digits(n):
    return len(str(abs(n)))

def check_armstrong(candidate):
    if candidate < 0:
        return False
    power = num_digits(candidate)
    running = 0
    remainder = candidate
    while remainder > 0:
        running += (remainder % 10) ** power
        remainder //= 10
    return running == candidate

def collect_armstrong(ceiling):
    if ceiling < 0:
        return []
    found = []
    for num in range(0, ceiling + 1):
        if check_armstrong(num):
            found.append(num)
    return found

def nearest_armstrong(n, ceiling):
    candidates = collect_armstrong(ceiling)
    closest = None
    min_dist = None
    for c in candidates:
        dist = abs(c - n)
        if min_dist is None or dist < min_dist:
            min_dist = dist
            closest = c
    return closest, min_dist

def narcissistic_report(ceiling):
    found = collect_armstrong(ceiling)
    print(f"Searching up to : {ceiling}")
    print(f"Armstrong nums  : {found}")
    print(f"Count found     : {len(found)}")
    for num in found:
        d = num_digits(num) if num > 0 else 1
        print(f"  {num} -> {d}-digit Armstrong number")
    sample = 200
    nearest, dist = nearest_armstrong(sample, ceiling)
    print(f"Nearest to {sample}   : {nearest} (distance {dist})")
    return found

narcissistic_report(1000)
