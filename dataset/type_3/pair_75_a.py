def total_steps(days):
    total = 0
    for item in days:
        total += item["steps"]
    return total

def average_steps(days):
    if not days:
        return 0
    return total_steps(days) / len(days)

def high_steps(days, minimum):
    selected = []
    for item in days:
        if item["steps"] >= minimum:
            selected.append(item)
    return selected

def step_report(days, minimum):
    total = total_steps(days)
    average = average_steps(days)
    selected = high_steps(days, minimum)
    print(f"Records         : {days}")
    print(f"Total steps  : {total}")
    print(f"Average steps: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_steps = [{"day": "Mon", "steps": 9000, "goal": 8000}, {"day": "Tue", "steps": 6500, "goal": 8000}]
step_report(example_steps, 10)
