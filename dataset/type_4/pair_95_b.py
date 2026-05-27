def total_aquarium(tanks):
    return sum(map(lambda entry: entry["temperature"], tanks))

def average_aquarium(tanks):
    values = tuple(entry["temperature"] for entry in tanks)
    return sum(values) / len(values) if values else 0

def maximum_aquarium(tanks):
    return max(tanks, key=lambda entry: entry["temperature"], default=None)

def select_aquarium(tanks, minimum):
    return list(filter(lambda entry: entry["temperature"] >= minimum, tanks))

def aquarium_report(tanks, minimum):
    summary = (
        total_aquarium(tanks),
        average_aquarium(tanks),
        maximum_aquarium(tanks),
        select_aquarium(tanks, minimum),
    )
    labels = ("Total temperature", "Average temperature", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_aquarium = [{"tank": "one", "temperature": 25}, {"tank": "two", "temperature": 27}, {"tank": "three", "temperature": 23}]
aquarium_report(data_aquarium, 10)
