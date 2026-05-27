def sum_logs_metric(records):
    amount = 0
    for row in records:
        if "severity" in row:
            amount += row["severity"]
    return amount

def mean_logs_metric(records):
    valid = [row for row in records if "severity" in row]
    if not valid:
        return 0
    return sum_logs_metric(valid) / len(valid)

def choose_logs_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("severity", 0)
        bonus = row.get("duration", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_logs_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("severity", 0) > best.get("severity", 0):
            best = row
    return best

def describe_logs(records, floor_value):
    cleaned = [row for row in records if row.get("severity", 0) >= 0]
    total = sum_logs_metric(cleaned)
    average = mean_logs_metric(cleaned)
    chosen = choose_logs_items(cleaned, floor_value)
    best = best_logs_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total severity  : {total}")
    print(f"Average severity: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_logs = [{"event": "login", "severity": 2, "duration": 5}, {"event": "sync", "severity": 4, "duration": 18}]
describe_logs(sample_logs, 10)
