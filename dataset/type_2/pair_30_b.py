def degrees_to_imperial(degrees):
    return degrees * 9 / 5 + 32

def imperial_to_degrees(imperial):
    return (imperial - 32) * 5 / 9

def heat_report(readings):
    changed = []
    for reading in readings:
        changed.append(degrees_to_imperial(reading))
    print(f"Metric scale: {readings}")
    print(f"Imperial scale: {changed}")
    return changed

heat_report([5, 18, 30])

def rounded_values(values):
    rounded = []
    for value in values:
        rounded.append(round(value, 2))
    return rounded

print(f"Rounded: {rounded_values(temperature_report([10, 15, 21]))}")

def describe_sample_size(values):
    size = 0
    for _ in values:
        size += 1
    if size == 0:
        return "empty"
    if size == 1:
        return "single"
    return "multiple"

print(describe_sample_size([1, 2, 3]))
