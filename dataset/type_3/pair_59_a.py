def total_transactions(entries):
    total = 0
    for item in entries:
        total += item["amount"]
    return total

def average_transactions(entries):
    if not entries:
        return 0
    return total_transactions(entries) / len(entries)

def high_transactions(entries, minimum):
    selected = []
    for item in entries:
        if item["amount"] >= minimum:
            selected.append(item)
    return selected

def transaction_report(entries, minimum):
    total = total_transactions(entries)
    average = average_transactions(entries)
    selected = high_transactions(entries, minimum)
    print(f"Records         : {entries}")
    print(f"Total amount  : {total}")
    print(f"Average amount: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_transactions = [{"id": 1, "amount": 120, "fee": 2}, {"id": 2, "amount": -45, "fee": 1}]
transaction_report(example_transactions, 10)
