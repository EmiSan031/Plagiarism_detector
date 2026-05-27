def sum_quiz_metric(records):
    amount = 0
    for row in records:
        if "correct" in row:
            amount += row["correct"]
    return amount

def mean_quiz_metric(records):
    valid = [row for row in records if "correct" in row]
    if not valid:
        return 0
    return sum_quiz_metric(valid) / len(valid)

def choose_quiz_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("correct", 0)
        bonus = row.get("points", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_quiz_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("correct", 0) > best.get("correct", 0):
            best = row
    return best

def describe_quiz(records, floor_value):
    cleaned = [row for row in records if row.get("correct", 0) >= 0]
    total = sum_quiz_metric(cleaned)
    average = mean_quiz_metric(cleaned)
    chosen = choose_quiz_items(cleaned, floor_value)
    best = best_quiz_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total correct  : {total}")
    print(f"Average correct: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_quiz = [{"q": 1, "correct": True, "points": 2}, {"q": 2, "correct": False, "points": 3}]
describe_quiz(sample_quiz, 10)
