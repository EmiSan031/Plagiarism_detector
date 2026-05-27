def compute_factorial(num):
    if num < 0:
        return None
    product = 1
    for step in range(2, num + 1):
        product *= step
    return product

def choose(total, select):
    if total < 0 or select < 0:
        return 0
    if select > total:
        return 0
    if select == 0 or select == total:
        return 1
    return compute_factorial(total) // (
        compute_factorial(select) * compute_factorial(total - select)
    )

def build_pascal_row(total):
    entries = []
    for sel in range(total + 1):
        entries.append(choose(total, sel))
    return entries

def build_pascal_triangle(rows):
    triangle = []
    for row_num in range(rows):
        triangle.append(build_pascal_row(row_num))
    return triangle

def choose_report(total, select):
    if total < 0 or select < 0:
        print(f"Invalid inputs: n={total}, k={select}")
        return 0
    outcome = choose(total, select)
    row = build_pascal_row(total)
    triangle = build_pascal_triangle(5)
    print(f"n               : {total}")
    print(f"k               : {select}")
    print(f"C({total}, {select})           : {outcome}")
    print(f"Pascal row {total}    : {row}")
    print(f"Row sum         : {sum(row)}")
    print(f"Row sum = 2^{total}  : {sum(row) == 2**total}")
    print(f"Pascal triangle (5 rows):")
    for r in triangle:
        print(f"  {r}")
    return outcome

choose_report(6, 2)
