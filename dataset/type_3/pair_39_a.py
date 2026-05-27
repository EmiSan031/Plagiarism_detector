def digit_count(number):
    n = abs(number)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

def digit_sum(number):
    n = abs(number)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def digit_report(number):
    count = digit_count(number)
    total = digit_sum(number)
    print(f"Number          : {number}")
    print(f"Digit count     : {count}")
    print(f"Digit sum       : {total}")
    print(f"Is negative     : {number < 0}")
    print(f"Last digit      : {abs(number) % 10}")
    print(f"First digit     : {int(str(abs(number))[0])}")
    return count, total

for num in [0, 7, 123, -4567, 99999]:
    digit_report(num)
    print()
