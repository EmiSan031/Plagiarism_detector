def make_histogram(values):
    histogram = {}
    for value in values:
        histogram[value] = histogram.get(value, 0) + 1
    return histogram

print(make_histogram(["red", "blue", "red"]))
