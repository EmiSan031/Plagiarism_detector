def total_budget(items):
    result = 0
    for item in items:
        result = result + item["amount"]
    return result

def average_budget(items):
    count = 0
    total = 0
    for item in items:
        count += 1
        total += item["amount"]
    if count == 0:
        return 0
    return total / count

def maximum_budget(items):
    if not items:
        return None
    best = items[0]
    for item in items[1:]:
        if item["amount"] > best["amount"]:
            best = item
    return best

def select_budget(items, minimum):
    selected = []
    for item in items:
        if item["amount"] >= minimum:
            selected.append(item)
    return selected

def budget_report(items, minimum):
    total = total_budget(items)
    average = average_budget(items)
    best = maximum_budget(items)
    selected = select_budget(items, minimum)
    print(f"Total amount: {total}")
    print(f"Average amount: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_budget = [{"name": "rent", "amount": 720}, {"name": "food", "amount": 310}, {"name": "bus", "amount": 45}]
budget_report(data_budget, 10)
