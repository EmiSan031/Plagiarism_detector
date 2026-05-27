def total_reimbursements(claims):
    total = 0
    for item in claims:
        total += item["cost"]
    return total

def average_reimbursements(claims):
    if not claims:
        return 0
    return total_reimbursements(claims) / len(claims)

def high_reimbursements(claims, minimum):
    selected = []
    for item in claims:
        if item["cost"] >= minimum:
            selected.append(item)
    return selected

def reimbursement_report(claims, minimum):
    total = total_reimbursements(claims)
    average = average_reimbursements(claims)
    selected = high_reimbursements(claims, minimum)
    print(f"Records         : {claims}")
    print(f"Total cost  : {total}")
    print(f"Average cost: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_reimbursements = [{"name": "taxi", "cost": 80, "approved": True}, {"name": "meal", "cost": 120, "approved": False}]
reimbursement_report(example_reimbursements, 10)
