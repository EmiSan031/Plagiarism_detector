def factorial(n):
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result

def count_permutations(n, r):
    if r > n:
        return 0
    return factorial(n) // factorial(n - r)

def count_combinations(n, r):
    if r > n:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))

def factorial_sum(n):
    total = 0
    for k in range(1, n + 1):
        total += factorial(k)
    return total

print(factorial(6))
print(factorial(0))
print(count_permutations(5, 2))
print(count_combinations(5, 2))
print(factorial_sum(4))
