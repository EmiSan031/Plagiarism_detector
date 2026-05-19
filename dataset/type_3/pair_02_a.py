def factorial(n):
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result

def show_factorial_table(limit):
    print(f"Factorial table up to {limit}:")
    print("-" * 28)
    for n in range(0, limit + 1):
        print(f"  {n}! = {factorial(n)}")
    print("-" * 28)

def digits_in_factorial(n):
    fact = factorial(n)
    return len(str(fact))

def factorial_report(n):
    show_factorial_table(n)
    result = factorial(n)
    print(f"Result of {n}!   : {result}")
    print(f"Digits in {n}!   : {digits_in_factorial(n)}")
    print(f"Is even         : {result % 2 == 0}")
    return result

factorial_report(6)
