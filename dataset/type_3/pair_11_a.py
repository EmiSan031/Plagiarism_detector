def binary_search(values, target):
    left = 0
    right = len(values) - 1
    while left <= right:
        middle = (left + right) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1

def binary_search_all(values, target):
    indices = []
    for index in range(len(values)):
        if values[index] == target:
            indices.append(index)
    return indices

def search_range(values, low, high):
    result = []
    for value in values:
        if low <= value <= high:
            result.append(value)
    return result

data = [1, 4, 7, 10, 10, 13, 17, 20]
print(binary_search(data, 10))
print(binary_search(data, 5))
print(binary_search_all(data, 10))
print(search_range(data, 5, 15))
