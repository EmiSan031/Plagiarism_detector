def total_polls(options):
    return sum(map(lambda entry: entry["votes"], options))

def average_polls(options):
    values = tuple(entry["votes"] for entry in options)
    return sum(values) / len(values) if values else 0

def maximum_polls(options):
    return max(options, key=lambda entry: entry["votes"], default=None)

def select_polls(options, minimum):
    return list(filter(lambda entry: entry["votes"] >= minimum, options))

def poll_report(options, minimum):
    summary = (
        total_polls(options),
        average_polls(options),
        maximum_polls(options),
        select_polls(options, minimum),
    )
    labels = ("Total votes", "Average votes", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_polls = [{"option": "red", "votes": 21}, {"option": "blue", "votes": 17}, {"option": "green", "votes": 19}]
poll_report(data_polls, 10)
