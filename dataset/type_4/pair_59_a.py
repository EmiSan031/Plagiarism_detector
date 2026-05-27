def total_transactions(entries):
    result = 0
    for item in entries:
        result = result + item["amount"]
    return result

def average_transactions(entries):
    count = 0
    total = 0
    for item in entries:
        count += 1
        total += item["amount"]
    if count == 0:
        return 0
    return total / count

def maximum_transactions(entries):
    if not entries:
        return None
    best = entries[0]
    for item in entries[1:]:
        if item["amount"] > best["amount"]:
            best = item
    return best

def select_transactions(entries, minimum):
    selected = []
    for item in entries:
        if item["amount"] >= minimum:
            selected.append(item)
    return selected

def transaction_report(entries, minimum):
    total = total_transactions(entries)
    average = average_transactions(entries)
    best = maximum_transactions(entries)
    selected = select_transactions(entries, minimum)
    print(f"Total amount: {total}")
    print(f"Average amount: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_transactions = [{"id": 1, "amount": 120}, {"id": 2, "amount": -45}, {"id": 3, "amount": 80}]
transaction_report(data_transactions, 10)
