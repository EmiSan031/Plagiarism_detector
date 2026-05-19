def fibonacci(n):
    sequence = []
    a = 0
    b = 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def fibonacci_at(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a

def is_fibonacci(n):
    sequence = fibonacci(20)
    return n in sequence

def fibonacci_sum(n):
    total = 0
    for value in fibonacci(n):
        total += value
    return total

print(fibonacci(8))
print(fibonacci_at(10))
print(is_fibonacci(13))
print(is_fibonacci(14))
print(fibonacci_sum(8))
