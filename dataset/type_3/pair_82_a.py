def total_medicine(doses):
    total = 0
    for item in doses:
        total += item["amount"]
    return total

def average_medicine(doses):
    if not doses:
        return 0
    return total_medicine(doses) / len(doses)

def high_medicine(doses, minimum):
    selected = []
    for item in doses:
        if item["amount"] >= minimum:
            selected.append(item)
    return selected

def medicine_report(doses, minimum):
    total = total_medicine(doses)
    average = average_medicine(doses)
    selected = high_medicine(doses, minimum)
    print(f"Records         : {doses}")
    print(f"Total amount  : {total}")
    print(f"Average amount: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_medicine = [{"name": "A", "amount": 2, "interval": 8}, {"name": "B", "amount": 1, "interval": 12}]
medicine_report(example_medicine, 10)
