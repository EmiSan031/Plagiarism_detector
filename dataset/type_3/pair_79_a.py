def total_classes(classes):
    total = 0
    for item in classes:
        total += item["students"]
    return total

def average_classes(classes):
    if not classes:
        return 0
    return total_classes(classes) / len(classes)

def high_classes(classes, minimum):
    selected = []
    for item in classes:
        if item["students"] >= minimum:
            selected.append(item)
    return selected

def class_report(classes, minimum):
    total = total_classes(classes)
    average = average_classes(classes)
    selected = high_classes(classes, minimum)
    print(f"Records         : {classes}")
    print(f"Total students  : {total}")
    print(f"Average students: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_classes = [{"room": "A", "students": 28, "capacity": 30}, {"room": "B", "students": 33, "capacity": 32}]
class_report(example_classes, 10)
