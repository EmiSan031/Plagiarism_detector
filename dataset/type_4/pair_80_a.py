def total_polls(options):
    result = 0
    for item in options:
        result = result + item["votes"]
    return result

def average_polls(options):
    count = 0
    total = 0
    for item in options:
        count += 1
        total += item["votes"]
    if count == 0:
        return 0
    return total / count

def maximum_polls(options):
    if not options:
        return None
    best = options[0]
    for item in options[1:]:
        if item["votes"] > best["votes"]:
            best = item
    return best

def select_polls(options, minimum):
    selected = []
    for item in options:
        if item["votes"] >= minimum:
            selected.append(item)
    return selected

def poll_report(options, minimum):
    total = total_polls(options)
    average = average_polls(options)
    best = maximum_polls(options)
    selected = select_polls(options, minimum)
    print(f"Total votes: {total}")
    print(f"Average votes: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_polls = [{"option": "red", "votes": 21}, {"option": "blue", "votes": 17}, {"option": "green", "votes": 19}]
poll_report(data_polls, 10)
