def triangular(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def square_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

def cube_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 3
    return total

def is_triangular(n):
    k = 1
    while triangular(k) < n:
        k += 1
    return triangular(k) == n

print(triangular(10))
print(square_sum(5))
print(cube_sum(4))
print(is_triangular(10))
print(is_triangular(11))
