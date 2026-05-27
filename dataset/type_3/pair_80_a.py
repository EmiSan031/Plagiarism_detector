def total_polls(options):
    total = 0
    for item in options:
        total += item["votes"]
    return total

def average_polls(options):
    if not options:
        return 0
    return total_polls(options) / len(options)

def high_polls(options, minimum):
    selected = []
    for item in options:
        if item["votes"] >= minimum:
            selected.append(item)
    return selected

def poll_report(options, minimum):
    total = total_polls(options)
    average = average_polls(options)
    selected = high_polls(options, minimum)
    print(f"Records         : {options}")
    print(f"Total votes  : {total}")
    print(f"Average votes: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_polls = [{"option": "red", "votes": 21, "rank": 1}, {"option": "blue", "votes": 17, "rank": 2}]
poll_report(example_polls, 10)
