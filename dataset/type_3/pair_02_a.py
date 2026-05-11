def factorial(n):
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result


print(factorial(6))
