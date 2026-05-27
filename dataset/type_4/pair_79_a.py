def total_classes(classes):
    result = 0
    for item in classes:
        result = result + item["students"]
    return result

def average_classes(classes):
    count = 0
    total = 0
    for item in classes:
        count += 1
        total += item["students"]
    if count == 0:
        return 0
    return total / count

def maximum_classes(classes):
    if not classes:
        return None
    best = classes[0]
    for item in classes[1:]:
        if item["students"] > best["students"]:
            best = item
    return best

def select_classes(classes, minimum):
    selected = []
    for item in classes:
        if item["students"] >= minimum:
            selected.append(item)
    return selected

def class_report(classes, minimum):
    total = total_classes(classes)
    average = average_classes(classes)
    best = maximum_classes(classes)
    selected = select_classes(classes, minimum)
    print(f"Total students: {total}")
    print(f"Average students: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_classes = [{"room": "A", "students": 28}, {"room": "B", "students": 33}, {"room": "C", "students": 22}]
class_report(data_classes, 10)
