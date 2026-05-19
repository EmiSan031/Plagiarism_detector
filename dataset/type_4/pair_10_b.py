def linear_search(values, target):
    try:
        return values.index(target)
    except ValueError:
        return -1

def linear_search_all(values, target):
    return [index for index, value in enumerate(values) if value == target]

def count_occurrences(values, target):
    return values.count(target)

def contains(values, target):
    return target in values

data = [3, 6, 9, 12, 6, 15, 6]
print(linear_search(data, 9))
print(linear_search(data, 99))
print(linear_search_all(data, 6))
print(count_occurrences(data, 6))
print(contains(data, 12))
