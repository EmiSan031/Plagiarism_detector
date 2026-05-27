def total_energy(meters):
    return sum(map(lambda entry: entry["kwh"], meters))

def average_energy(meters):
    values = tuple(entry["kwh"] for entry in meters)
    return sum(values) / len(values) if values else 0

def maximum_energy(meters):
    return max(meters, key=lambda entry: entry["kwh"], default=None)

def select_energy(meters, minimum):
    return list(filter(lambda entry: entry["kwh"] >= minimum, meters))

def energy_report(meters, minimum):
    summary = (
        total_energy(meters),
        average_energy(meters),
        maximum_energy(meters),
        select_energy(meters, minimum),
    )
    labels = ("Total kwh", "Average kwh", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_energy = [{"meter": "M1", "kwh": 120}, {"meter": "M2", "kwh": 95}, {"meter": "M3", "kwh": 150}]
energy_report(data_energy, 10)
