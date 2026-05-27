def sum_budget_metric(records):
    amount = 0
    for row in records:
        if "amount" in row:
            amount += row["amount"]
    return amount

def mean_budget_metric(records):
    valid = [row for row in records if "amount" in row]
    if not valid:
        return 0
    return sum_budget_metric(valid) / len(valid)

def choose_budget_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("amount", 0)
        bonus = row.get("limit", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_budget_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("amount", 0) > best.get("amount", 0):
            best = row
    return best

def describe_budget(records, floor_value):
    cleaned = [row for row in records if row.get("amount", 0) >= 0]
    total = sum_budget_metric(cleaned)
    average = mean_budget_metric(cleaned)
    chosen = choose_budget_items(cleaned, floor_value)
    best = best_budget_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total amount  : {total}")
    print(f"Average amount: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_budget = [{"name": "rent", "amount": 720, "limit": 800}, {"name": "food", "amount": 310, "limit": 350}]
describe_budget(sample_budget, 10)
