def total_groceries(items):
    result = 0
    for item in items:
        result = result + item["quantity"]
    return result

def average_groceries(items):
    count = 0
    total = 0
    for item in items:
        count += 1
        total += item["quantity"]
    if count == 0:
        return 0
    return total / count

def maximum_groceries(items):
    if not items:
        return None
    best = items[0]
    for item in items[1:]:
        if item["quantity"] > best["quantity"]:
            best = item
    return best

def select_groceries(items, minimum):
    selected = []
    for item in items:
        if item["quantity"] >= minimum:
            selected.append(item)
    return selected

def grocery_report(items, minimum):
    total = total_groceries(items)
    average = average_groceries(items)
    best = maximum_groceries(items)
    selected = select_groceries(items, minimum)
    print(f"Total quantity: {total}")
    print(f"Average quantity: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_groceries = [{"name": "rice", "quantity": 3}, {"name": "beans", "quantity": 2}, {"name": "oil", "quantity": 1}]
grocery_report(data_groceries, 10)
