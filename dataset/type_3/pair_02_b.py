def product_until(limit):
    if limit < 0:
        return None
    answer = 1
    current_values = range(2, limit + 1)
    for factor in current_values:
        answer *= factor
    return answer

def display_product_table(upper):
    print(f"Product table up to {upper}:")
    print("-" * 28)
    for n in range(0, upper + 1):
        val = product_until(n)
        if val is not None:
            print(f"  {n}! = {val}")
    print("-" * 28)

def count_digits(limit):
    val = product_until(limit)
    if val is None:
        return 0
    return len(str(val))

def product_report(limit):
    display_product_table(limit)
    outcome = product_until(limit)
    if outcome is None:
        print(f"Invalid input: {limit}")
        return None
    print(f"Result of {limit}!  : {outcome}")
    print(f"Digits in {limit}!  : {count_digits(limit)}")
    print(f"Is even         : {outcome % 2 == 0}")
    return outcome

product_report(6)
