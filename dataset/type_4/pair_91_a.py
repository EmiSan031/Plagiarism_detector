def total_energy(meters):
    result = 0
    for item in meters:
        result = result + item["kwh"]
    return result

def average_energy(meters):
    count = 0
    total = 0
    for item in meters:
        count += 1
        total += item["kwh"]
    if count == 0:
        return 0
    return total / count

def maximum_energy(meters):
    if not meters:
        return None
    best = meters[0]
    for item in meters[1:]:
        if item["kwh"] > best["kwh"]:
            best = item
    return best

def select_energy(meters, minimum):
    selected = []
    for item in meters:
        if item["kwh"] >= minimum:
            selected.append(item)
    return selected

def energy_report(meters, minimum):
    total = total_energy(meters)
    average = average_energy(meters)
    best = maximum_energy(meters)
    selected = select_energy(meters, minimum)
    print(f"Total kwh: {total}")
    print(f"Average kwh: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_energy = [{"meter": "M1", "kwh": 120}, {"meter": "M2", "kwh": 95}, {"meter": "M3", "kwh": 150}]
energy_report(data_energy, 10)
