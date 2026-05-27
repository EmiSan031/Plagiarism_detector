def sum_leaderboard_metric(records):
    amount = 0
    for row in records:
        if "points" in row:
            amount += row["points"]
    return amount

def mean_leaderboard_metric(records):
    valid = [row for row in records if "points" in row]
    if not valid:
        return 0
    return sum_leaderboard_metric(valid) / len(valid)

def choose_leaderboard_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("points", 0)
        bonus = row.get("wins", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_leaderboard_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("points", 0) > best.get("points", 0):
            best = row
    return best

def describe_leaderboard(records, floor_value):
    cleaned = [row for row in records if row.get("points", 0) >= 0]
    total = sum_leaderboard_metric(cleaned)
    average = mean_leaderboard_metric(cleaned)
    chosen = choose_leaderboard_items(cleaned, floor_value)
    best = best_leaderboard_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total points  : {total}")
    print(f"Average points: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_leaderboard = [{"name": "Kai", "points": 31, "wins": 4}, {"name": "Mia", "points": 28, "wins": 5}]
describe_leaderboard(sample_leaderboard, 10)
