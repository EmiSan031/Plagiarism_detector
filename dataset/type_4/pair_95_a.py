def total_aquarium(tanks):
    result = 0
    for item in tanks:
        result = result + item["temperature"]
    return result

def average_aquarium(tanks):
    count = 0
    total = 0
    for item in tanks:
        count += 1
        total += item["temperature"]
    if count == 0:
        return 0
    return total / count

def maximum_aquarium(tanks):
    if not tanks:
        return None
    best = tanks[0]
    for item in tanks[1:]:
        if item["temperature"] > best["temperature"]:
            best = item
    return best

def select_aquarium(tanks, minimum):
    selected = []
    for item in tanks:
        if item["temperature"] >= minimum:
            selected.append(item)
    return selected

def aquarium_report(tanks, minimum):
    total = total_aquarium(tanks)
    average = average_aquarium(tanks)
    best = maximum_aquarium(tanks)
    selected = select_aquarium(tanks, minimum)
    print(f"Total temperature: {total}")
    print(f"Average temperature: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_aquarium = [{"tank": "one", "temperature": 25}, {"tank": "two", "temperature": 27}, {"tank": "three", "temperature": 23}]
aquarium_report(data_aquarium, 10)
