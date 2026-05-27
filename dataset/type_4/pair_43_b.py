def triangular(n):
    return n * (n + 1) // 2

def square_sum(n):
    return n * (n + 1) * (2 * n + 1) // 6

def cube_sum(n):
    return (n * (n + 1) // 2) ** 2

def is_triangular(n):
    discriminant = 1 + 8 * n
    root = int(discriminant ** 0.5)
    return root * root == discriminant and (root - 1) % 2 == 0

print(triangular(10))
print(square_sum(5))
print(cube_sum(4))
print(is_triangular(10))
print(is_triangular(11))
