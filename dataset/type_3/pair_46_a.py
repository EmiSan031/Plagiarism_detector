def digit_count(n):
    return len(str(abs(n)))

def is_armstrong(n):
    if n < 0:
        return False
    digits = digit_count(n)
    total = 0
    temp = n
    while temp > 0:
        total += (temp % 10) ** digits
        temp //= 10
    return total == n

def armstrong_numbers_up_to(limit):
    result = []
    for number in range(0, limit + 1):
        if is_armstrong(number):
            result.append(number)
    return result

def armstrong_report(limit):
    numbers = armstrong_numbers_up_to(limit)
    print(f"Searching up to : {limit}")
    print(f"Armstrong nums  : {numbers}")
    print(f"Count found     : {len(numbers)}")
    for num in numbers:
        d = digit_count(num) if num > 0 else 1
        print(f"  {num} -> {d}-digit Armstrong number")
    return numbers

armstrong_report(1000)
