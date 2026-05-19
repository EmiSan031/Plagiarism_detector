def factorial(n):
    result = 1
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return None
    if n == 0:
        print("Factorial of 0 is 1 by definition.")
        return 1
    for value in range(2, n + 1):
        result *= value
    return result

def show_factorial_table(limit):
    print(f"Factorial table from 0 to {limit}:")
    print("-" * 30)
    for n in range(0, limit + 1):
        res = factorial(n)
        if res is not None:
            print(f"  {n}! = {res}")
    print("-" * 30)

target = 6
show_factorial_table(target)
single = factorial(target)
print(f"Factorial of {target}: {single}")
