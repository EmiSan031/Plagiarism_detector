def get_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

def is_perfect(n):
    if n < 2:
        return False
    return sum(get_divisors(n)) == n

def perfect_numbers_up_to(limit):
    perfect = []
    for number in range(2, limit + 1):
        if is_perfect(number):
            perfect.append(number)
    return perfect

def perfect_report(limit):
    perfect = perfect_numbers_up_to(limit)
    print(f"Searching up to : {limit}")
    print(f"Perfect numbers : {perfect}")
    print(f"Count found     : {len(perfect)}")
    for p in perfect:
        divs = get_divisors(p)
        print(f"  {p} -> divisors: {divs} -> sum: {sum(divs)}")
    return perfect

perfect_report(500)
