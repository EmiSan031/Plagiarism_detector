def sum_subscriptions_metric(records):
    amount = 0
    for row in records:
        if "monthly" in row:
            amount += row["monthly"]
    return amount

def mean_subscriptions_metric(records):
    valid = [row for row in records if "monthly" in row]
    if not valid:
        return 0
    return sum_subscriptions_metric(valid) / len(valid)

def choose_subscriptions_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("monthly", 0)
        bonus = row.get("users", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_subscriptions_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("monthly", 0) > best.get("monthly", 0):
            best = row
    return best

def describe_subscriptions(records, floor_value):
    cleaned = [row for row in records if row.get("monthly", 0) >= 0]
    total = sum_subscriptions_metric(cleaned)
    average = mean_subscriptions_metric(cleaned)
    chosen = choose_subscriptions_items(cleaned, floor_value)
    best = best_subscriptions_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total monthly  : {total}")
    print(f"Average monthly: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_subscriptions = [{"plan": "basic", "monthly": 9, "users": 14}, {"plan": "team", "monthly": 18, "users": 8}]
describe_subscriptions(sample_subscriptions, 10)
