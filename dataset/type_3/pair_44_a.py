def tribonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 0]
    sequence = [0, 0, 1]
    for _ in range(3, n):
        next_val = sequence[-1] + sequence[-2] + sequence[-3]
        sequence.append(next_val)
    return sequence[:n]

def tribonacci_sum(n):
    total = 0
    for val in tribonacci(n):
        total += val
    return total

def tribonacci_report(n):
    sequence = tribonacci(n)
    total = tribonacci_sum(n)
    print(f"Terms requested : {n}")
    print(f"Sequence        : {sequence}")
    print(f"Last term       : {sequence[-1]}")
    print(f"Sum of terms    : {total}")
    even_count = sum(1 for v in sequence if v % 2 == 0)
    print(f"Even terms      : {even_count}")
    print(f"Odd terms       : {n - even_count}")
    return sequence

tribonacci_report(10)
