def total_donations(gifts):
    result = 0
    for item in gifts:
        result = result + item["amount"]
    return result

def average_donations(gifts):
    count = 0
    total = 0
    for item in gifts:
        count += 1
        total += item["amount"]
    if count == 0:
        return 0
    return total / count

def maximum_donations(gifts):
    if not gifts:
        return None
    best = gifts[0]
    for item in gifts[1:]:
        if item["amount"] > best["amount"]:
            best = item
    return best

def select_donations(gifts, minimum):
    selected = []
    for item in gifts:
        if item["amount"] >= minimum:
            selected.append(item)
    return selected

def donation_report(gifts, minimum):
    total = total_donations(gifts)
    average = average_donations(gifts)
    best = maximum_donations(gifts)
    selected = select_donations(gifts, minimum)
    print(f"Total amount: {total}")
    print(f"Average amount: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_donations = [{"donor": "A", "amount": 60}, {"donor": "B", "amount": 45}, {"donor": "C", "amount": 90}]
donation_report(data_donations, 10)
