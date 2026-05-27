def total_medicine(doses):
    return sum(map(lambda entry: entry["amount"], doses))

def average_medicine(doses):
    values = tuple(entry["amount"] for entry in doses)
    return sum(values) / len(values) if values else 0

def maximum_medicine(doses):
    return max(doses, key=lambda entry: entry["amount"], default=None)

def select_medicine(doses, minimum):
    return list(filter(lambda entry: entry["amount"] >= minimum, doses))

def medicine_report(doses, minimum):
    summary = (
        total_medicine(doses),
        average_medicine(doses),
        maximum_medicine(doses),
        select_medicine(doses, minimum),
    )
    labels = ("Total amount", "Average amount", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_medicine = [{"name": "A", "amount": 2}, {"name": "B", "amount": 1}, {"name": "C", "amount": 4}]
medicine_report(data_medicine, 10)
