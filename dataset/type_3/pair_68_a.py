def total_leaderboard(players):
    total = 0
    for item in players:
        total += item["points"]
    return total

def average_leaderboard(players):
    if not players:
        return 0
    return total_leaderboard(players) / len(players)

def high_leaderboard(players, minimum):
    selected = []
    for item in players:
        if item["points"] >= minimum:
            selected.append(item)
    return selected

def leaderboard_report(players, minimum):
    total = total_leaderboard(players)
    average = average_leaderboard(players)
    selected = high_leaderboard(players, minimum)
    print(f"Records         : {players}")
    print(f"Total points  : {total}")
    print(f"Average points: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_leaderboard = [{"name": "Kai", "points": 31, "wins": 4}, {"name": "Mia", "points": 28, "wins": 5}]
leaderboard_report(example_leaderboard, 10)
