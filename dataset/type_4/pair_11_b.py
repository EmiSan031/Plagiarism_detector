def binary_search(values, target):
    matches = [i for i, v in enumerate(values) if v == target]
    return matches[0] if matches else -1

def binary_search_all(values, target):
    return [i for i, v in enumerate(values) if v == target]

def search_range(values, low, high):
    return list(filter(lambda v: low <= v <= high, values))

def count_in_range(values, low, high):
    return sum(1 for v in values if low <= v <= high)

def closest_to(values, target):
    return min(values, key=lambda v: abs(v - target))

def search_sorted(values, target):
    return target in values

data = [1, 4, 7, 10, 10, 13, 17, 20]
print(binary_search(data, 10))
print(binary_search(data, 5))
print(binary_search_all(data, 10))
print(search_range(data, 5, 15))
print(count_in_range(data, 5, 15))
print(closest_to(data, 9))
print(search_sorted(data, 13))
