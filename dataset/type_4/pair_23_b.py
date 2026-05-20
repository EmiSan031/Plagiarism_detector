def completed_tasks(tasks):
    return [task["title"] for task in tasks if task["done"]]

def pending_tasks(tasks):
    return [task["title"] for task in tasks if not task["done"]]

def task_report(tasks):
    groups = {
        "completed": completed_tasks(tasks),
        "pending": pending_tasks(tasks),
    }
    print("Completed:", len(groups["completed"]))
    print("Pending:", len(groups["pending"]))
    return groups["completed"], groups["pending"]

tasks = [{"title": "read", "done": True}, {"title": "write", "done": False}]
task_report(tasks)

def task_titles(tasks):
    titles = []
    for task in tasks:
        titles.append(task.get("title", task.get("name", "")))
    return titles

print(f"All tasks: {task_titles(tasks) if 'tasks' in globals() else task_titles(jobs)}")

def describe_sample_size(values):
    size = 0
    for _ in values:
        size += 1
    if size == 0:
        return "empty"
    if size == 1:
        return "single"
    return "multiple"

print(describe_sample_size([1, 2, 3]))
