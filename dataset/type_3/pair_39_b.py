def count_digits(n):
    value = abs(n)
    if value == 0:
        return 1
    tally = 0
    while value > 0:
        value //= 10
        tally += 1
    return tally

def sum_of_digits(n):
    value = abs(n)
    running = 0
    while value > 0:
        running += value % 10
        value //= 10
    return running

def product_of_digits(n):
    value = abs(n)
    if value == 0:
        return 0
    product = 1
    while value > 0:
        product *= value % 10
        value //= 10
    return product

def number_report(n):
    tally = count_digits(n)
    digit_sum = sum_of_digits(n)
    digit_prod = product_of_digits(n)
    print(f"Number          : {n}")
    print(f"Digit count     : {tally}")
    print(f"Digit sum       : {digit_sum}")
    print(f"Digit product   : {digit_prod}")
    print(f"Is negative     : {n < 0}")
    print(f"Last digit      : {abs(n) % 10}")
    print(f"First digit     : {int(str(abs(n))[0])}")
    return tally, digit_sum

for num in [0, 7, 123, -4567, 99999]:
    number_report(num)
    print()
