def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def count_permutations(n, r):
    if r > n:
        return 0
    return factorial(n) // factorial(n - r)

def count_combinations(n, r):
    if r > n:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))

def factorial_sum(n):
    if n <= 0:
        return 0
    return factorial(n) + factorial_sum(n - 1)

print(factorial(6))
print(factorial(0))
print(count_permutations(5, 2))
print(count_combinations(5, 2))
print(factorial_sum(4))
