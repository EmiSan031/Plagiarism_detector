def completed_tasks(tasks):
    result = []
    for task in tasks:
        if task["done"]:
            result.append(task["title"])
    return result

def pending_tasks(tasks):
    result = []
    for task in tasks:
        if not task["done"]:
            result.append(task["title"])
    return result

def task_report(tasks):
    done = completed_tasks(tasks)
    pending = pending_tasks(tasks)
    print(f"Completed: {len(done)}")
    print(f"Pending: {len(pending)}")
    return done, pending

tasks = [{"title": "read", "done": True}, {"title": "write", "done": False}]
task_report(tasks)

def task_titles(tasks):
    titles = []
    for task in tasks:
        titles.append(task.get("title", task.get("name", "")))
    return titles

print(f"All tasks: {task_titles(tasks) if 'tasks' in globals() else task_titles(jobs)}")
