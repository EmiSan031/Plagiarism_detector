def total_steps(days):
    return sum(map(lambda entry: entry["steps"], days))

def average_steps(days):
    values = tuple(entry["steps"] for entry in days)
    return sum(values) / len(values) if values else 0

def maximum_steps(days):
    return max(days, key=lambda entry: entry["steps"], default=None)

def select_steps(days, minimum):
    return list(filter(lambda entry: entry["steps"] >= minimum, days))

def step_report(days, minimum):
    summary = (
        total_steps(days),
        average_steps(days),
        maximum_steps(days),
        select_steps(days, minimum),
    )
    labels = ("Total steps", "Average steps", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_steps = [{"day": "Mon", "steps": 9000}, {"day": "Tue", "steps": 6500}, {"day": "Wed", "steps": 10200}]
step_report(data_steps, 10)
