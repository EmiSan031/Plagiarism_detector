def total_bakery(batches):
    return sum(map(lambda entry: entry["loaves"], batches))

def average_bakery(batches):
    values = tuple(entry["loaves"] for entry in batches)
    return sum(values) / len(values) if values else 0

def maximum_bakery(batches):
    return max(batches, key=lambda entry: entry["loaves"], default=None)

def select_bakery(batches, minimum):
    return list(filter(lambda entry: entry["loaves"] >= minimum, batches))

def bakery_report(batches, minimum):
    summary = (
        total_bakery(batches),
        average_bakery(batches),
        maximum_bakery(batches),
        select_bakery(batches, minimum),
    )
    labels = ("Total loaves", "Average loaves", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_bakery = [{"batch": "morning", "loaves": 80}, {"batch": "noon", "loaves": 65}, {"batch": "night", "loaves": 72}]
bakery_report(data_bakery, 10)
