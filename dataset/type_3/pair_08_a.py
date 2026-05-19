def fibonacci(n):
    sequence = []
    a = 0
    b = 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def is_in_sequence(num, n):
    return num in fibonacci(n)

def sum_fibonacci(n):
    total = 0
    for val in fibonacci(n):
        total += val
    return total

def fibonacci_report(n):
    sequence = fibonacci(n)
    print(f"Terms requested : {n}")
    print(f"Sequence        : {sequence}")
    print(f"First term      : {sequence[0]}")
    print(f"Last term       : {sequence[-1]}")
    print(f"Sum of terms    : {sum_fibonacci(n)}")
    even_count = sum(1 for v in sequence if v % 2 == 0)
    print(f"Even terms      : {even_count}")
    print(f"Is 13 in seq?   : {is_in_sequence(13, n)}")
    return sequence

fibonacci_report(8)
