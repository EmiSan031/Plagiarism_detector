def total_groceries(items):
    total = 0
    for item in items:
        total += item["quantity"]
    return total

def average_groceries(items):
    if not items:
        return 0
    return total_groceries(items) / len(items)

def high_groceries(items, minimum):
    selected = []
    for item in items:
        if item["quantity"] >= minimum:
            selected.append(item)
    return selected

def grocery_report(items, minimum):
    total = total_groceries(items)
    average = average_groceries(items)
    selected = high_groceries(items, minimum)
    print(f"Records         : {items}")
    print(f"Total quantity  : {total}")
    print(f"Average quantity: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_groceries = [{"name": "rice", "quantity": 3, "price": 24}, {"name": "beans", "quantity": 2, "price": 18}]
grocery_report(example_groceries, 10)
