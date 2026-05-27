def total_sensors(samples):
    result = 0
    for item in samples:
        result = result + item["value"]
    return result

def average_sensors(samples):
    count = 0
    total = 0
    for item in samples:
        count += 1
        total += item["value"]
    if count == 0:
        return 0
    return total / count

def maximum_sensors(samples):
    if not samples:
        return None
    best = samples[0]
    for item in samples[1:]:
        if item["value"] > best["value"]:
            best = item
    return best

def select_sensors(samples, minimum):
    selected = []
    for item in samples:
        if item["value"] >= minimum:
            selected.append(item)
    return selected

def sensor_report(samples, minimum):
    total = total_sensors(samples)
    average = average_sensors(samples)
    best = maximum_sensors(samples)
    selected = select_sensors(samples, minimum)
    print(f"Total value: {total}")
    print(f"Average value: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_sensors = [{"id": "s1", "value": 72}, {"id": "s2", "value": 91}, {"id": "s3", "value": 64}]
sensor_report(data_sensors, 10)
