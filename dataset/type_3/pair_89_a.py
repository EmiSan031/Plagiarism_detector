def total_donations(gifts):
    total = 0
    for item in gifts:
        total += item["amount"]
    return total

def average_donations(gifts):
    if not gifts:
        return 0
    return total_donations(gifts) / len(gifts)

def high_donations(gifts, minimum):
    selected = []
    for item in gifts:
        if item["amount"] >= minimum:
            selected.append(item)
    return selected

def donation_report(gifts, minimum):
    total = total_donations(gifts)
    average = average_donations(gifts)
    selected = high_donations(gifts, minimum)
    print(f"Records         : {gifts}")
    print(f"Total amount  : {total}")
    print(f"Average amount: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_donations = [{"donor": "A", "amount": 60, "matched": 20}, {"donor": "B", "amount": 45, "matched": 0}]
donation_report(example_donations, 10)
