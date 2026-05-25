def clamp_values(values, low, high):
    result = []
    for value in values:
        result.append(max(low, min(high, value)))
    return result

print(clamp_values([-2, 4, 12], 0, 10))
