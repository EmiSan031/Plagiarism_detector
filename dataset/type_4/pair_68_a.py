def total_leaderboard(players):
    result = 0
    for item in players:
        result = result + item["points"]
    return result

def average_leaderboard(players):
    count = 0
    total = 0
    for item in players:
        count += 1
        total += item["points"]
    if count == 0:
        return 0
    return total / count

def maximum_leaderboard(players):
    if not players:
        return None
    best = players[0]
    for item in players[1:]:
        if item["points"] > best["points"]:
            best = item
    return best

def select_leaderboard(players, minimum):
    selected = []
    for item in players:
        if item["points"] >= minimum:
            selected.append(item)
    return selected

def leaderboard_report(players, minimum):
    total = total_leaderboard(players)
    average = average_leaderboard(players)
    best = maximum_leaderboard(players)
    selected = select_leaderboard(players, minimum)
    print(f"Total points: {total}")
    print(f"Average points: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_leaderboard = [{"name": "Kai", "points": 31}, {"name": "Mia", "points": 28}, {"name": "Zoe", "points": 35}]
leaderboard_report(data_leaderboard, 10)
