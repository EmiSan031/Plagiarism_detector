def moving_total(values):
    total = 0
    result = []
    for value in values:
        total += value
        result.append(total)
    return result

print(moving_total([3, 1, 4]))
