def runner_up(data):
    if len(data) < 2:
        return None
    leader = second = None
    for entry in data:
        if leader is None or entry > leader:
            second = leader
            leader = entry
        elif second is None or (entry > second and entry != leader):
            second = entry
    return second

def top_three(data):
    if len(data) < 3:
        return None
    first = runner_up(data)
    leader = max(data)
    remaining = []
    for entry in data:
        if entry != leader and entry != first:
            remaining.append(entry)
    third = max(remaining) if remaining else None
    return leader, first, third

def podium_report(data):
    if len(data) < 2:
        print("Not enough elements for ranking.")
        return None
    leader = max(data)
    second = runner_up(data)
    top = top_three(data)
    print(f"Dataset         : {data}")
    print(f"Count           : {len(data)}")
    print(f"1st place       : {leader}")
    print(f"2nd place       : {second}")
    if top and top[2] is not None:
        print(f"3rd place       : {top[2]}")
    if second is not None:
        print(f"Gap (1st - 2nd) : {leader - second}")
    running = 0
    for v in data:
        running += v
    print(f"Sum             : {running}")
    return second

podium_report([4, 1, 9, 3, 9, 7, 2])
