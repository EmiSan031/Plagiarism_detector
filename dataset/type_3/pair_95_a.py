def total_aquarium(tanks):
    total = 0
    for item in tanks:
        total += item["ph"]
    return total

def average_aquarium(tanks):
    if not tanks:
        return 0
    return total_aquarium(tanks) / len(tanks)

def high_aquarium(tanks, minimum):
    selected = []
    for item in tanks:
        if item["ph"] >= minimum:
            selected.append(item)
    return selected

def aquarium_report(tanks, minimum):
    total = total_aquarium(tanks)
    average = average_aquarium(tanks)
    selected = high_aquarium(tanks, minimum)
    print(f"Records         : {tanks}")
    print(f"Total ph  : {total}")
    print(f"Average ph: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_aquarium = [{"tank": "one", "ph": 7.1, "temperature": 25}, {"tank": "two", "ph": 6.6, "temperature": 27}]
aquarium_report(example_aquarium, 10)
