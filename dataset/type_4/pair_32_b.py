def digit_sum(n):
    return sum(int(d) for d in str(abs(n)))

def digital_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

def count_digits(n):
    return len(str(abs(n)))

def reverse_digits(n):
    negative = n < 0
    reversed_str = str(abs(n))[::-1]
    return -int(reversed_str) if negative else int(reversed_str)

print(digit_sum(1234))
print(digit_sum(-987))
print(digital_root(9875))
print(count_digits(10000))
print(reverse_digits(12345))
