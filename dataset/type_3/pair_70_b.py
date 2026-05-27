def sum_emails_metric(records):
    amount = 0
    for row in records:
        if "size" in row:
            amount += row["size"]
    return amount

def mean_emails_metric(records):
    valid = [row for row in records if "size" in row]
    if not valid:
        return 0
    return sum_emails_metric(valid) / len(valid)

def choose_emails_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("size", 0)
        bonus = row.get("attachments", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_emails_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("size", 0) > best.get("size", 0):
            best = row
    return best

def describe_emails(records, floor_value):
    cleaned = [row for row in records if row.get("size", 0) >= 0]
    total = sum_emails_metric(cleaned)
    average = mean_emails_metric(cleaned)
    chosen = choose_emails_items(cleaned, floor_value)
    best = best_emails_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total size  : {total}")
    print(f"Average size: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_emails = [{"sender": "a@x.com", "size": 18, "attachments": 1}, {"sender": "b@y.com", "size": 9, "attachments": 0}]
describe_emails(sample_emails, 10)
