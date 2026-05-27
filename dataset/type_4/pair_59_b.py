def total_transactions(entries):
    return sum(map(lambda entry: entry["amount"], entries))

def average_transactions(entries):
    values = tuple(entry["amount"] for entry in entries)
    return sum(values) / len(values) if values else 0

def maximum_transactions(entries):
    return max(entries, key=lambda entry: entry["amount"], default=None)

def select_transactions(entries, minimum):
    return list(filter(lambda entry: entry["amount"] >= minimum, entries))

def transaction_report(entries, minimum):
    summary = (
        total_transactions(entries),
        average_transactions(entries),
        maximum_transactions(entries),
        select_transactions(entries, minimum),
    )
    labels = ("Total amount", "Average amount", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_transactions = [{"id": 1, "amount": 120}, {"id": 2, "amount": -45}, {"id": 3, "amount": 80}]
transaction_report(data_transactions, 10)
