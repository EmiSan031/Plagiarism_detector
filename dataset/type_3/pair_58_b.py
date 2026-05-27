def sum_exams_metric(records):
    amount = 0
    for row in records:
        if "score" in row:
            amount += row["score"]
    return amount

def mean_exams_metric(records):
    valid = [row for row in records if "score" in row]
    if not valid:
        return 0
    return sum_exams_metric(valid) / len(valid)

def choose_exams_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("score", 0)
        bonus = row.get("bonus", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_exams_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("score", 0) > best.get("score", 0):
            best = row
    return best

def describe_exams(records, floor_value):
    cleaned = [row for row in records if row.get("score", 0) >= 0]
    total = sum_exams_metric(cleaned)
    average = mean_exams_metric(cleaned)
    chosen = choose_exams_items(cleaned, floor_value)
    best = best_exams_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total score  : {total}")
    print(f"Average score: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_exams = [{"student": "Nora", "score": 82, "bonus": 3}, {"student": "Omar", "score": 71, "bonus": 5}]
describe_exams(sample_exams, 10)
