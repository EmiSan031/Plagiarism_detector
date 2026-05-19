def linear_search(values, target):
    # Return the first matching index.
    for index in range(len(values)):
        if values[index] == target:
            return index
    return -1

# Return all positions where target appears.
def linear_search_all(values, target):
    indices = []
    for index in range(len(values)):
        if values[index] == target:
            indices.append(index)
    return indices

def count_occurrences(values, target):
    count = 0
    for value in values:
        if value == target:
            count += 1
    return count

def contains(values, target):
    for value in values:
        if value == target:
            return True
    return False

data = [3, 6, 9, 12, 6, 15, 6]
print(linear_search(data, 9))
print(linear_search(data, 99))
print(linear_search_all(data, 6))
print(count_occurrences(data, 6))
print(contains(data, 12))
print(contains(data, 50))
