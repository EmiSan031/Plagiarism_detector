def total_soccer(teams):
    return sum(map(lambda entry: entry["goals"], teams))

def average_soccer(teams):
    values = tuple(entry["goals"] for entry in teams)
    return sum(values) / len(values) if values else 0

def maximum_soccer(teams):
    return max(teams, key=lambda entry: entry["goals"], default=None)

def select_soccer(teams, minimum):
    return list(filter(lambda entry: entry["goals"] >= minimum, teams))

def soccer_report(teams, minimum):
    summary = (
        total_soccer(teams),
        average_soccer(teams),
        maximum_soccer(teams),
        select_soccer(teams, minimum),
    )
    labels = ("Total goals", "Average goals", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_soccer = [{"team": "Lions", "goals": 9}, {"team": "Waves", "goals": 7}, {"team": "Stars", "goals": 11}]
soccer_report(data_soccer, 10)
