def total_queue(jobs):
    result = 0
    for item in jobs:
        result = result + item["minutes"]
    return result

def average_queue(jobs):
    count = 0
    total = 0
    for item in jobs:
        count += 1
        total += item["minutes"]
    if count == 0:
        return 0
    return total / count

def maximum_queue(jobs):
    if not jobs:
        return None
    best = jobs[0]
    for item in jobs[1:]:
        if item["minutes"] > best["minutes"]:
            best = item
    return best

def select_queue(jobs, minimum):
    selected = []
    for item in jobs:
        if item["minutes"] >= minimum:
            selected.append(item)
    return selected

def queue_report(jobs, minimum):
    total = total_queue(jobs)
    average = average_queue(jobs)
    best = maximum_queue(jobs)
    selected = select_queue(jobs, minimum)
    print(f"Total minutes: {total}")
    print(f"Average minutes: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_queue = [{"job": "print", "minutes": 6}, {"job": "scan", "minutes": 3}, {"job": "backup", "minutes": 12}]
queue_report(data_queue, 10)
