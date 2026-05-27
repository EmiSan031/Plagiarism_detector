def sum_courses_metric(records):
    amount = 0
    for row in records:
        if "credits" in row:
            amount += row["credits"]
    return amount

def mean_courses_metric(records):
    valid = [row for row in records if "credits" in row]
    if not valid:
        return 0
    return sum_courses_metric(valid) / len(valid)

def choose_courses_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("credits", 0)
        bonus = row.get("passed", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_courses_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("credits", 0) > best.get("credits", 0):
            best = row
    return best

def describe_courses(records, floor_value):
    cleaned = [row for row in records if row.get("credits", 0) >= 0]
    total = sum_courses_metric(cleaned)
    average = mean_courses_metric(cleaned)
    chosen = choose_courses_items(cleaned, floor_value)
    best = best_courses_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total credits  : {total}")
    print(f"Average credits: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_courses = [{"code": "CS1", "credits": 6, "passed": True}, {"code": "MA1", "credits": 5, "passed": False}]
describe_courses(sample_courses, 10)
