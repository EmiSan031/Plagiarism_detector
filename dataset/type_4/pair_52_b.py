def total_budget(items):
    return sum(map(lambda entry: entry["amount"], items))

def average_budget(items):
    values = tuple(entry["amount"] for entry in items)
    return sum(values) / len(values) if values else 0

def maximum_budget(items):
    return max(items, key=lambda entry: entry["amount"], default=None)

def select_budget(items, minimum):
    return list(filter(lambda entry: entry["amount"] >= minimum, items))

def budget_report(items, minimum):
    summary = (
        total_budget(items),
        average_budget(items),
        maximum_budget(items),
        select_budget(items, minimum),
    )
    labels = ("Total amount", "Average amount", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_budget = [{"name": "rent", "amount": 720}, {"name": "food", "amount": 310}, {"name": "bus", "amount": 45}]
budget_report(data_budget, 10)
