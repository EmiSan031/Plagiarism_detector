def total_queue(jobs):
    return sum(map(lambda entry: entry["minutes"], jobs))

def average_queue(jobs):
    values = tuple(entry["minutes"] for entry in jobs)
    return sum(values) / len(values) if values else 0

def maximum_queue(jobs):
    return max(jobs, key=lambda entry: entry["minutes"], default=None)

def select_queue(jobs, minimum):
    return list(filter(lambda entry: entry["minutes"] >= minimum, jobs))

def queue_report(jobs, minimum):
    summary = (
        total_queue(jobs),
        average_queue(jobs),
        maximum_queue(jobs),
        select_queue(jobs, minimum),
    )
    labels = ("Total minutes", "Average minutes", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_queue = [{"job": "print", "minutes": 6}, {"job": "scan", "minutes": 3}, {"job": "backup", "minutes": 12}]
queue_report(data_queue, 10)
