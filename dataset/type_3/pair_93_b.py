def sum_reimbursements_metric(records):
    amount = 0
    for row in records:
        if "cost" in row:
            amount += row["cost"]
    return amount

def mean_reimbursements_metric(records):
    valid = [row for row in records if "cost" in row]
    if not valid:
        return 0
    return sum_reimbursements_metric(valid) / len(valid)

def choose_reimbursements_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("cost", 0)
        bonus = row.get("approved", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_reimbursements_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("cost", 0) > best.get("cost", 0):
            best = row
    return best

def describe_reimbursements(records, floor_value):
    cleaned = [row for row in records if row.get("cost", 0) >= 0]
    total = sum_reimbursements_metric(cleaned)
    average = mean_reimbursements_metric(cleaned)
    chosen = choose_reimbursements_items(cleaned, floor_value)
    best = best_reimbursements_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total cost  : {total}")
    print(f"Average cost: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_reimbursements = [{"name": "taxi", "cost": 80, "approved": True}, {"name": "meal", "cost": 120, "approved": False}]
describe_reimbursements(sample_reimbursements, 10)
