def total_queue(jobs):
    total = 0
    for item in jobs:
        total += item["minutes"]
    return total

def average_queue(jobs):
    if not jobs:
        return 0
    return total_queue(jobs) / len(jobs)

def high_queue(jobs, minimum):
    selected = []
    for item in jobs:
        if item["minutes"] >= minimum:
            selected.append(item)
    return selected

def queue_report(jobs, minimum):
    total = total_queue(jobs)
    average = average_queue(jobs)
    selected = high_queue(jobs, minimum)
    print(f"Records         : {jobs}")
    print(f"Total minutes  : {total}")
    print(f"Average minutes: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_queue = [{"job": "print", "minutes": 6, "priority": 2}, {"job": "scan", "minutes": 3, "priority": 1}]
queue_report(example_queue, 10)
