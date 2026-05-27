def sum_polls_metric(records):
    amount = 0
    for row in records:
        if "votes" in row:
            amount += row["votes"]
    return amount

def mean_polls_metric(records):
    valid = [row for row in records if "votes" in row]
    if not valid:
        return 0
    return sum_polls_metric(valid) / len(valid)

def choose_polls_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("votes", 0)
        bonus = row.get("rank", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_polls_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("votes", 0) > best.get("votes", 0):
            best = row
    return best

def describe_polls(records, floor_value):
    cleaned = [row for row in records if row.get("votes", 0) >= 0]
    total = sum_polls_metric(cleaned)
    average = mean_polls_metric(cleaned)
    chosen = choose_polls_items(cleaned, floor_value)
    best = best_polls_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total votes  : {total}")
    print(f"Average votes: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_polls = [{"option": "red", "votes": 21, "rank": 1}, {"option": "blue", "votes": 17, "rank": 2}]
describe_polls(sample_polls, 10)
