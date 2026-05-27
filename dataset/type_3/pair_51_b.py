def sum_attendance_metric(records):
    amount = 0
    for row in records:
        if "present" in row:
            amount += row["present"]
    return amount

def mean_attendance_metric(records):
    valid = [row for row in records if "present" in row]
    if not valid:
        return 0
    return sum_attendance_metric(valid) / len(valid)

def choose_attendance_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("present", 0)
        bonus = row.get("total", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_attendance_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("present", 0) > best.get("present", 0):
            best = row
    return best

def describe_attendance(records, floor_value):
    cleaned = [row for row in records if row.get("present", 0) >= 0]
    total = sum_attendance_metric(cleaned)
    average = mean_attendance_metric(cleaned)
    chosen = choose_attendance_items(cleaned, floor_value)
    best = best_attendance_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total present  : {total}")
    print(f"Average present: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_attendance = [{"student": "Ana", "present": 17, "total": 20}, {"student": "Luis", "present": 14, "total": 18}]
describe_attendance(sample_attendance, 10)
