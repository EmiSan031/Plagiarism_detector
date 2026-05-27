def total_budget(items):
    total = 0
    for item in items:
        total += item["amount"]
    return total

def average_budget(items):
    if not items:
        return 0
    return total_budget(items) / len(items)

def high_budget(items, minimum):
    selected = []
    for item in items:
        if item["amount"] >= minimum:
            selected.append(item)
    return selected

def budget_report(items, minimum):
    total = total_budget(items)
    average = average_budget(items)
    selected = high_budget(items, minimum)
    print(f"Records         : {items}")
    print(f"Total amount  : {total}")
    print(f"Average amount: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_budget = [{"name": "rent", "amount": 720, "limit": 800}, {"name": "food", "amount": 310, "limit": 350}]
budget_report(example_budget, 10)
