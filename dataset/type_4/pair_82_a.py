def total_medicine(doses):
    result = 0
    for item in doses:
        result = result + item["amount"]
    return result

def average_medicine(doses):
    count = 0
    total = 0
    for item in doses:
        count += 1
        total += item["amount"]
    if count == 0:
        return 0
    return total / count

def maximum_medicine(doses):
    if not doses:
        return None
    best = doses[0]
    for item in doses[1:]:
        if item["amount"] > best["amount"]:
            best = item
    return best

def select_medicine(doses, minimum):
    selected = []
    for item in doses:
        if item["amount"] >= minimum:
            selected.append(item)
    return selected

def medicine_report(doses, minimum):
    total = total_medicine(doses)
    average = average_medicine(doses)
    best = maximum_medicine(doses)
    selected = select_medicine(doses, minimum)
    print(f"Total amount: {total}")
    print(f"Average amount: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_medicine = [{"name": "A", "amount": 2}, {"name": "B", "amount": 1}, {"name": "C", "amount": 4}]
medicine_report(data_medicine, 10)
