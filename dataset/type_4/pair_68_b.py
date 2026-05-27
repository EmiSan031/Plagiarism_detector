def total_leaderboard(players):
    return sum(map(lambda entry: entry["points"], players))

def average_leaderboard(players):
    values = tuple(entry["points"] for entry in players)
    return sum(values) / len(values) if values else 0

def maximum_leaderboard(players):
    return max(players, key=lambda entry: entry["points"], default=None)

def select_leaderboard(players, minimum):
    return list(filter(lambda entry: entry["points"] >= minimum, players))

def leaderboard_report(players, minimum):
    summary = (
        total_leaderboard(players),
        average_leaderboard(players),
        maximum_leaderboard(players),
        select_leaderboard(players, minimum),
    )
    labels = ("Total points", "Average points", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_leaderboard = [{"name": "Kai", "points": 31}, {"name": "Mia", "points": 28}, {"name": "Zoe", "points": 35}]
leaderboard_report(data_leaderboard, 10)
