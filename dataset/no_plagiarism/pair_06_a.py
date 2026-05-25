def rolling_average(numbers, window):
    result = []
    for index in range(len(numbers) - window + 1):
        result.append(sum(numbers[index:index + window]) / window)
    return result

print(rolling_average([2, 4, 6, 8, 10], 3))
