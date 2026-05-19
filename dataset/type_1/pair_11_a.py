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

def binary_search_first(values, target):
    index = binary_search(values, target)
    if index == -1:
        return -1
    while index > 0 and values[index - 1] == target:
        index -= 1
    return index

def binary_search_last(values, target):
    index = binary_search(values, target)
    if index == -1:
        return -1
    while index < len(values) - 1 and values[index + 1] == target:
        index += 1
    return index

data = [1, 4, 7, 10, 10, 10, 13]
print(binary_search(data, 10))
print(binary_search(data, 5))
print(binary_search_first(data, 10))
print(binary_search_last(data, 10))
