def total_tasks(tasks):
    total = 0
    for item in tasks:
        total += item["done"]
    return total

def average_tasks(tasks):
    if not tasks:
        return 0
    return total_tasks(tasks) / len(tasks)

def high_tasks(tasks, minimum):
    selected = []
    for item in tasks:
        if item["done"] >= minimum:
            selected.append(item)
    return selected

def task_report(tasks, minimum):
    total = total_tasks(tasks)
    average = average_tasks(tasks)
    selected = high_tasks(tasks, minimum)
    print(f"Records         : {tasks}")
    print(f"Total done  : {total}")
    print(f"Average done: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_tasks = [{"title": "draft", "done": True, "priority": 2}, {"title": "test", "done": False, "priority": 5}]
task_report(example_tasks, 10)
