def completed_tasks(tasks):
    result = []
    for task in tasks:
        if task["done"]:
            result.append(task["title"])
    result.sort()
    return result

def pending_tasks(tasks):
    result = []
    for task in tasks:
        if not task["done"]:
            result.append(task["title"])
    result.sort()
    return result

def overdue_tasks(tasks):
    result = []
    for task in tasks:
        if not task["done"] and task.get("overdue", False):
            result.append(task["title"])
    return result

def task_report(tasks):
    done = completed_tasks(tasks)
    pending = pending_tasks(tasks)
    overdue = overdue_tasks(tasks)
    print(f"Completed: {len(done)}")
    print(f"Pending: {len(pending)}")
    print(f"Overdue: {len(overdue)}")
    return done, pending

tasks = [{"title": "read", "done": True}, {"title": "write", "done": False, "overdue": True}]
task_report(tasks)
