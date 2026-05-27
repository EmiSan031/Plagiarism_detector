def total_soccer(teams):
    result = 0
    for item in teams:
        result = result + item["goals"]
    return result

def average_soccer(teams):
    count = 0
    total = 0
    for item in teams:
        count += 1
        total += item["goals"]
    if count == 0:
        return 0
    return total / count

def maximum_soccer(teams):
    if not teams:
        return None
    best = teams[0]
    for item in teams[1:]:
        if item["goals"] > best["goals"]:
            best = item
    return best

def select_soccer(teams, minimum):
    selected = []
    for item in teams:
        if item["goals"] >= minimum:
            selected.append(item)
    return selected

def soccer_report(teams, minimum):
    total = total_soccer(teams)
    average = average_soccer(teams)
    best = maximum_soccer(teams)
    selected = select_soccer(teams, minimum)
    print(f"Total goals: {total}")
    print(f"Average goals: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_soccer = [{"team": "Lions", "goals": 9}, {"team": "Waves", "goals": 7}, {"team": "Stars", "goals": 11}]
soccer_report(data_soccer, 10)
