def select_even(values):
    selected = []
    for item in values:
        if item % 2 == 0:
            selected.append(item)
    return selected

def select_odd(values):
    selected = []
    for item in values:
        if item % 2 != 0:
            selected.append(item)
    return selected

def parity_report(values):
    if not values:
        print("The collection is empty.")
        return
    even_items = select_even(values)
    odd_items = select_odd(values)
    print(f"Input collection: {values}")
    print(f"Total entries   : {len(values)}")
    print(f"Even entries    : {even_items}")
    print(f"Even count      : {len(even_items)}")
    print(f"Odd entries     : {odd_items}")
    print(f"Odd count       : {len(odd_items)}")
    even_total = 0
    for item in even_items:
        even_total += item
    odd_total = 0
    for item in odd_items:
        odd_total += item
    print(f"Sum of evens    : {even_total}")
    print(f"Sum of odds     : {odd_total}")

parity_report([10, 11, 12, 13, 14, 15])
