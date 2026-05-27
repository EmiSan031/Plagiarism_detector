def gcd_two(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm_two(a, b):
    return (a * b) // gcd_two(a, b)

def gcd_list(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result = gcd_two(result, number)
    return result

def lcm_list(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result = lcm_two(result, number)
    return result

def gcd_lcm_report(numbers):
    gcd = gcd_list(numbers)
    lcm = lcm_list(numbers)
    print(f"Numbers         : {numbers}")
    print(f"Count           : {len(numbers)}")
    print(f"GCD of all      : {gcd}")
    print(f"LCM of all      : {lcm}")
    print(f"All divisible   : {all(n % gcd == 0 for n in numbers)}")
    print(f"LCM / GCD ratio : {lcm // gcd}")
    return gcd, lcm

gcd_lcm_report([12, 18, 24, 36])
