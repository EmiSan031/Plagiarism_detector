def binary_search(values, target):
    matches = [index for index, value in enumerate(values) if value == target]
    return matches[0] if matches else -1


print(binary_search([1, 4, 7, 10, 13], 10))
