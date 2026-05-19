def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def gcd_list(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result = gcd(result, number)
    return result

def lcm_list(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result = lcm(result, number)
    return result

def are_coprime(a, b):
    return gcd(a, b) == 1

print(gcd(84, 30))
print(lcm(4, 6))
print(gcd_list([84, 30, 18]))
print(lcm_list([4, 6, 10]))
print(are_coprime(8, 9))
print(are_coprime(8, 4))
