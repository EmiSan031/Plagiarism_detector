def closest_value(values, target):
    best = values[0]
    for value in values[1:]:
        if abs(value - target) < abs(best - target):
            best = value
    return best

print(closest_value([2, 8, 13, 21], 10))
