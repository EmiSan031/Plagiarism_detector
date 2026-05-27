def digit_sum(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def digital_root(n):
    while n >= 10:
        n = digit_sum(n)
    return n

def count_digits(n):
    count = 0
    n = abs(n)
    if n == 0:
        return 1
    while n > 0:
        count += 1
        n //= 10
    return count

def reverse_digits(n):
    negative = n < 0
    n = abs(n)
    result = 0
    while n > 0:
        result = result * 10 + n % 10
        n //= 10
    return -result if negative else result

print(digit_sum(1234))
print(digit_sum(-987))
print(digital_root(9875))
print(count_digits(10000))
print(reverse_digits(12345))
