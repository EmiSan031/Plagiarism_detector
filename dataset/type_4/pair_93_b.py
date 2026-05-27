def total_reimbursements(claims):
    return sum(map(lambda entry: entry["cost"], claims))

def average_reimbursements(claims):
    values = tuple(entry["cost"] for entry in claims)
    return sum(values) / len(values) if values else 0

def maximum_reimbursements(claims):
    return max(claims, key=lambda entry: entry["cost"], default=None)

def select_reimbursements(claims, minimum):
    return list(filter(lambda entry: entry["cost"] >= minimum, claims))

def reimbursement_report(claims, minimum):
    summary = (
        total_reimbursements(claims),
        average_reimbursements(claims),
        maximum_reimbursements(claims),
        select_reimbursements(claims, minimum),
    )
    labels = ("Total cost", "Average cost", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_reimbursements = [{"name": "taxi", "cost": 80}, {"name": "meal", "cost": 120}, {"name": "hotel", "cost": 300}]
reimbursement_report(data_reimbursements, 10)
