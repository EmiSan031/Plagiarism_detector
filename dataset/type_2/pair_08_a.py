def fibonacci(n):
    sequence = []
    a = 0
    b = 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def is_fibonacci_number(num):
    sequence = fibonacci(50)
    return num in sequence

def print_fibonacci_report(n):
    sequence = fibonacci(n)
    print(f"Fibonacci sequence ({n} terms): {sequence}")
    print(f"First term : {sequence[0]}")
    print(f"Last term  : {sequence[-1]}")
    total = 0
    for val in sequence:
        total += val
    print(f"Sum of all terms: {total}")
    even_count = 0
    for val in sequence:
        if val % 2 == 0:
            even_count += 1
    print(f"Even numbers in sequence: {even_count}")
    print(f"Is 21 a Fibonacci number? {is_fibonacci_number(21)}")
    print(f"Is 22 a Fibonacci number? {is_fibonacci_number(22)}")

print_fibonacci_report(8)
