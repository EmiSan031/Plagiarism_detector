def total_tasks(tasks):
    result = 0
    for item in tasks:
        result = result + item["priority"]
    return result

def average_tasks(tasks):
    count = 0
    total = 0
    for item in tasks:
        count += 1
        total += item["priority"]
    if count == 0:
        return 0
    return total / count

def maximum_tasks(tasks):
    if not tasks:
        return None
    best = tasks[0]
    for item in tasks[1:]:
        if item["priority"] > best["priority"]:
            best = item
    return best

def select_tasks(tasks, minimum):
    selected = []
    for item in tasks:
        if item["priority"] >= minimum:
            selected.append(item)
    return selected

def task_report(tasks, minimum):
    total = total_tasks(tasks)
    average = average_tasks(tasks)
    best = maximum_tasks(tasks)
    selected = select_tasks(tasks, minimum)
    print(f"Total priority: {total}")
    print(f"Average priority: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_tasks = [{"title": "draft", "priority": 2}, {"title": "test", "priority": 5}, {"title": "ship", "priority": 4}]
task_report(data_tasks, 10)
