def total_sensors(samples):
    total = 0
    for item in samples:
        total += item["value"]
    return total

def average_sensors(samples):
    if not samples:
        return 0
    return total_sensors(samples) / len(samples)

def high_sensors(samples, minimum):
    selected = []
    for item in samples:
        if item["value"] >= minimum:
            selected.append(item)
    return selected

def sensor_report(samples, minimum):
    total = total_sensors(samples)
    average = average_sensors(samples)
    selected = high_sensors(samples, minimum)
    print(f"Records         : {samples}")
    print(f"Total value  : {total}")
    print(f"Average value: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_sensors = [{"id": "s1", "value": 72, "threshold": 80}, {"id": "s2", "value": 91, "threshold": 85}]
sensor_report(example_sensors, 10)
