def total_soccer(teams):
    total = 0
    for item in teams:
        total += item["goals"]
    return total

def average_soccer(teams):
    if not teams:
        return 0
    return total_soccer(teams) / len(teams)

def high_soccer(teams, minimum):
    selected = []
    for item in teams:
        if item["goals"] >= minimum:
            selected.append(item)
    return selected

def soccer_report(teams, minimum):
    total = total_soccer(teams)
    average = average_soccer(teams)
    selected = high_soccer(teams, minimum)
    print(f"Records         : {teams}")
    print(f"Total goals  : {total}")
    print(f"Average goals: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_soccer = [{"team": "Lions", "goals": 9, "points": 12}, {"team": "Waves", "goals": 7, "points": 10}]
soccer_report(example_soccer, 10)
