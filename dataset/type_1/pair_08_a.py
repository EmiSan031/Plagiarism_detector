def fibonacci(n):
    sequence = []
    a = 0
    b = 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


print(fibonacci(8))
