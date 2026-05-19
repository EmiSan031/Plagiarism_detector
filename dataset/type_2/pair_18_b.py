def repeated_multiply(value, times):
    product = 1
    for _ in range(times):
        product *= value
    return product

def multiplication_table(value, max_times):
    entries = []
    for t in range(0, max_times + 1):
        entries.append((t, repeated_multiply(value, t)))
    return entries

def check_perfect_square(num):
    if num < 0:
        return False
    root = int(num ** 0.5)
    return repeated_multiply(root, 2) == num

def multiplication_report(value, times):
    if times < 0:
        print("Only non-negative repetitions are supported.")
        return
    product = repeated_multiply(value, times)
    print(f"Value           : {value}")
    print(f"Times           : {times}")
    print(f"Result          : {value}^{times} = {product}")
    print(f"Multiplication table for {value}:")
    for t, val in multiplication_table(value, times):
        print(f"  {value}^{t} = {val}")
    print(f"Is result a perfect square? {check_perfect_square(product)}")

multiplication_report(2, 5)
