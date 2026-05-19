def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def gcd_list(numbers):
    if len(numbers) == 1:
        return numbers[0]
    return gcd(numbers[0], gcd_list(numbers[1:]))

def lcm_list(numbers):
    if len(numbers) == 1:
        return numbers[0]
    return lcm(numbers[0], lcm_list(numbers[1:]))

def are_coprime(a, b):
    return gcd(a, b) == 1

print(gcd(84, 30))
print(lcm(4, 6))
print(gcd_list([84, 30, 18]))
print(lcm_list([4, 6, 10]))
print(are_coprime(8, 9))
