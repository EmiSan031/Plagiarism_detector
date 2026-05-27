def total_classes(classes):
    return sum(map(lambda entry: entry["students"], classes))

def average_classes(classes):
    values = tuple(entry["students"] for entry in classes)
    return sum(values) / len(values) if values else 0

def maximum_classes(classes):
    return max(classes, key=lambda entry: entry["students"], default=None)

def select_classes(classes, minimum):
    return list(filter(lambda entry: entry["students"] >= minimum, classes))

def class_report(classes, minimum):
    summary = (
        total_classes(classes),
        average_classes(classes),
        maximum_classes(classes),
        select_classes(classes, minimum),
    )
    labels = ("Total students", "Average students", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_classes = [{"room": "A", "students": 28}, {"room": "B", "students": 33}, {"room": "C", "students": 22}]
class_report(data_classes, 10)
