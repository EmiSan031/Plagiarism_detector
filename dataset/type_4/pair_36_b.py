def to_binary(n):
    return bin(n)[2:]

def to_octal(n):
    return oct(n)[2:]

def to_hexadecimal(n):
    return hex(n)[2:].upper()

def count_ones(n):
    return bin(n).count("1")

def to_base(n, base):
    digits = "0123456789ABCDEF"
    if n == 0:
        return "0"
    result = ""
    while n:
        result = digits[n % base] + result
        n //= base
    return result

print(to_binary(42))
print(to_octal(42))
print(to_hexadecimal(255))
print(count_ones(42))
print(to_base(255, 16))
print(to_base(42, 2))
