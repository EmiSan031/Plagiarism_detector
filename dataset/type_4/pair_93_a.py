def total_reimbursements(claims):
    result = 0
    for item in claims:
        result = result + item["cost"]
    return result

def average_reimbursements(claims):
    count = 0
    total = 0
    for item in claims:
        count += 1
        total += item["cost"]
    if count == 0:
        return 0
    return total / count

def maximum_reimbursements(claims):
    if not claims:
        return None
    best = claims[0]
    for item in claims[1:]:
        if item["cost"] > best["cost"]:
            best = item
    return best

def select_reimbursements(claims, minimum):
    selected = []
    for item in claims:
        if item["cost"] >= minimum:
            selected.append(item)
    return selected

def reimbursement_report(claims, minimum):
    total = total_reimbursements(claims)
    average = average_reimbursements(claims)
    best = maximum_reimbursements(claims)
    selected = select_reimbursements(claims, minimum)
    print(f"Total cost: {total}")
    print(f"Average cost: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_reimbursements = [{"name": "taxi", "cost": 80}, {"name": "meal", "cost": 120}, {"name": "hotel", "cost": 300}]
reimbursement_report(data_reimbursements, 10)
