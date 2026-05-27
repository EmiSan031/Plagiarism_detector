def to_binary(n):
    if n == 0:
        return "0"
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    return "".join(reversed(bits))

def to_octal(n):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % 8))
        n //= 8
    return "".join(reversed(digits))

def to_hexadecimal(n):
    hex_chars = "0123456789ABCDEF"
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(hex_chars[n % 16])
        n //= 16
    return "".join(reversed(digits))

def count_ones(n):
    binary = to_binary(n)
    count = 0
    for bit in binary:
        if bit == "1":
            count += 1
    return count

print(to_binary(42))
print(to_octal(42))
print(to_hexadecimal(255))
print(count_ones(42))
