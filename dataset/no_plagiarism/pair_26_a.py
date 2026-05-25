def remove_outliers(values, limit):
    average = sum(values) / len(values)
    return [value for value in values if abs(value - average) <= limit]

print(remove_outliers([10, 11, 12, 100], 20))
