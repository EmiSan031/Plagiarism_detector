def product_until(limit):
    answer = 1
    if limit < 0:
        print("Operation undefined for negative inputs.")
        return None
    if limit == 0:
        print("Base case: product_until(0) returns 1.")
        return 1
    for factor in range(2, limit + 1):
        answer *= factor
    return answer

def display_product_table(upper_bound):
    print(f"Product table from 0 to {upper_bound}:")
    print("-" * 30)
    for num in range(0, upper_bound + 1):
        val = product_until(num)
        if val is not None:
            print(f"  {num}! = {val}")
    print("-" * 30)

chosen = 5
display_product_table(chosen)
outcome = product_until(chosen)
print(f"Product until {chosen}: {outcome}")
