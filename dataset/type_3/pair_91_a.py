def total_energy(meters):
    total = 0
    for item in meters:
        total += item["kwh"]
    return total

def average_energy(meters):
    if not meters:
        return 0
    return total_energy(meters) / len(meters)

def high_energy(meters, minimum):
    selected = []
    for item in meters:
        if item["kwh"] >= minimum:
            selected.append(item)
    return selected

def energy_report(meters, minimum):
    total = total_energy(meters)
    average = average_energy(meters)
    selected = high_energy(meters, minimum)
    print(f"Records         : {meters}")
    print(f"Total kwh  : {total}")
    print(f"Average kwh: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_energy = [{"meter": "M1", "kwh": 120, "rate": 1.5}, {"meter": "M2", "kwh": 95, "rate": 1.7}]
energy_report(example_energy, 10)
