def total_steps(days):
    result = 0
    for item in days:
        result = result + item["steps"]
    return result

def average_steps(days):
    count = 0
    total = 0
    for item in days:
        count += 1
        total += item["steps"]
    if count == 0:
        return 0
    return total / count

def maximum_steps(days):
    if not days:
        return None
    best = days[0]
    for item in days[1:]:
        if item["steps"] > best["steps"]:
            best = item
    return best

def select_steps(days, minimum):
    selected = []
    for item in days:
        if item["steps"] >= minimum:
            selected.append(item)
    return selected

def step_report(days, minimum):
    total = total_steps(days)
    average = average_steps(days)
    best = maximum_steps(days)
    selected = select_steps(days, minimum)
    print(f"Total steps: {total}")
    print(f"Average steps: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_steps = [{"day": "Mon", "steps": 9000}, {"day": "Tue", "steps": 6500}, {"day": "Wed", "steps": 10200}]
step_report(data_steps, 10)
