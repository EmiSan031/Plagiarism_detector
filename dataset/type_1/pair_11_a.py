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


print(binary_search([1, 4, 7, 10, 13], 10))
