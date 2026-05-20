def finished_jobs(jobs):
    output = []
    for job in jobs:
        if job["finished"]:
            output.append(job["name"])
    return output

def open_jobs(jobs):
    output = []
    for job in jobs:
        if not job["finished"]:
            output.append(job["name"])
    return output

def job_summary(jobs):
    finished = finished_jobs(jobs)
    open_list = open_jobs(jobs)
    print(f"Done jobs: {len(finished)}")
    print(f"Open jobs: {len(open_list)}")
    return finished, open_list

jobs = [{"name": "plan", "finished": True}, {"name": "test", "finished": False}]
job_summary(jobs)

def task_titles(tasks):
    titles = []
    for task in tasks:
        titles.append(task.get("title", task.get("name", "")))
    return titles

print(f"All tasks: {task_titles(tasks) if 'tasks' in globals() else task_titles(jobs)}")
