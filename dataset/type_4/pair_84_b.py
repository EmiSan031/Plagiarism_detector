def total_irrigation(plots):
    return sum(map(lambda entry: entry["liters"], plots))

def average_irrigation(plots):
    values = tuple(entry["liters"] for entry in plots)
    return sum(values) / len(values) if values else 0

def maximum_irrigation(plots):
    return max(plots, key=lambda entry: entry["liters"], default=None)

def select_irrigation(plots, minimum):
    return list(filter(lambda entry: entry["liters"] >= minimum, plots))

def irrigation_report(plots, minimum):
    summary = (
        total_irrigation(plots),
        average_irrigation(plots),
        maximum_irrigation(plots),
        select_irrigation(plots, minimum),
    )
    labels = ("Total liters", "Average liters", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_irrigation = [{"plot": "east", "liters": 300}, {"plot": "west", "liters": 260}, {"plot": "north", "liters": 410}]
irrigation_report(data_irrigation, 10)
