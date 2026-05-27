def total_groceries(items):
    return sum(map(lambda entry: entry["quantity"], items))

def average_groceries(items):
    values = tuple(entry["quantity"] for entry in items)
    return sum(values) / len(values) if values else 0

def maximum_groceries(items):
    return max(items, key=lambda entry: entry["quantity"], default=None)

def select_groceries(items, minimum):
    return list(filter(lambda entry: entry["quantity"] >= minimum, items))

def grocery_report(items, minimum):
    summary = (
        total_groceries(items),
        average_groceries(items),
        maximum_groceries(items),
        select_groceries(items, minimum),
    )
    labels = ("Total quantity", "Average quantity", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_groceries = [{"name": "rice", "quantity": 3}, {"name": "beans", "quantity": 2}, {"name": "oil", "quantity": 1}]
grocery_report(data_groceries, 10)
