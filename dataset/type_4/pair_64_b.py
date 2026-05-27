def total_sensors(samples):
    return sum(map(lambda entry: entry["value"], samples))

def average_sensors(samples):
    values = tuple(entry["value"] for entry in samples)
    return sum(values) / len(values) if values else 0

def maximum_sensors(samples):
    return max(samples, key=lambda entry: entry["value"], default=None)

def select_sensors(samples, minimum):
    return list(filter(lambda entry: entry["value"] >= minimum, samples))

def sensor_report(samples, minimum):
    summary = (
        total_sensors(samples),
        average_sensors(samples),
        maximum_sensors(samples),
        select_sensors(samples, minimum),
    )
    labels = ("Total value", "Average value", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_sensors = [{"id": "s1", "value": 72}, {"id": "s2", "value": 91}, {"id": "s3", "value": 64}]
sensor_report(data_sensors, 10)
