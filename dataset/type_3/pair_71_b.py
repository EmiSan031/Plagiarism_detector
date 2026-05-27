def sum_files_metric(records):
    amount = 0
    for row in records:
        if "bytes" in row:
            amount += row["bytes"]
    return amount

def mean_files_metric(records):
    valid = [row for row in records if "bytes" in row]
    if not valid:
        return 0
    return sum_files_metric(valid) / len(valid)

def choose_files_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("bytes", 0)
        bonus = row.get("age", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_files_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("bytes", 0) > best.get("bytes", 0):
            best = row
    return best

def describe_files(records, floor_value):
    cleaned = [row for row in records if row.get("bytes", 0) >= 0]
    total = sum_files_metric(cleaned)
    average = mean_files_metric(cleaned)
    chosen = choose_files_items(cleaned, floor_value)
    best = best_files_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total bytes  : {total}")
    print(f"Average bytes: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_files = [{"path": "a.txt", "bytes": 1200, "age": 4}, {"path": "b.log", "bytes": 5400, "age": 12}]
describe_files(sample_files, 10)
