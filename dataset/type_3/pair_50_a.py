def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def combination(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return factorial(n) // (factorial(k) * factorial(n - k))

def pascal_row(n):
    row = []
    for k in range(n + 1):
        row.append(combination(n, k))
    return row

def combination_report(n, k):
    result = combination(n, k)
    row = pascal_row(n)
    print(f"n               : {n}")
    print(f"k               : {k}")
    print(f"C({n}, {k})           : {result}")
    print(f"Pascal row {n}    : {row}")
    print(f"Row sum         : {sum(row)}")
    print(f"Row sum = 2^{n}  : {sum(row) == 2**n}")
    return result

combination_report(6, 2)
