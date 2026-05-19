def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

def power_table(base, max_exp):
    table = []
    for exp in range(0, max_exp + 1):
        table.append((exp, power(base, exp)))
    return table

def is_perfect_square(n):
    if n < 0:
        return False
    root = int(n ** 0.5)
    return power(root, 2) == n

def power_report(base, exponent):
    if exponent < 0:
        print("This implementation only supports non-negative exponents.")
        return
    result = power(base, exponent)
    print(f"Base            : {base}")
    print(f"Exponent        : {exponent}")
    print(f"Result          : {base}^{exponent} = {result}")
    print(f"Power table for base {base}:")
    for exp, val in power_table(base, exponent):
        print(f"  {base}^{exp} = {val}")
    print(f"Is result a perfect square? {is_perfect_square(result)}")

power_report(3, 4)
