def total_tasks(tasks):
    return sum(map(lambda entry: entry["priority"], tasks))

def average_tasks(tasks):
    values = tuple(entry["priority"] for entry in tasks)
    return sum(values) / len(values) if values else 0

def maximum_tasks(tasks):
    return max(tasks, key=lambda entry: entry["priority"], default=None)

def select_tasks(tasks, minimum):
    return list(filter(lambda entry: entry["priority"] >= minimum, tasks))

def task_report(tasks, minimum):
    summary = (
        total_tasks(tasks),
        average_tasks(tasks),
        maximum_tasks(tasks),
        select_tasks(tasks, minimum),
    )
    labels = ("Total priority", "Average priority", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_tasks = [{"title": "draft", "priority": 2}, {"title": "test", "priority": 5}, {"title": "ship", "priority": 4}]
task_report(data_tasks, 10)
