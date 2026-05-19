# Keep the first occurrence only.
def remove_duplicates(values):
    result = []

    for value in values:
        if value not in result:
            result.append(value)
    return result
def count_duplicates(values):
    count = 0
    seen = []
    for value in values:
        if value in seen:
            count += 1
        else:
            seen.append(value)
    return count
def has_duplicates(values):
    seen = []
    for value in values:
        if value in seen:
            return True
        seen.append(value)
    return False
def get_duplicates(values):
    duplicates = []
    seen = []
    for value in values:
        if value in seen and value not in duplicates:
            duplicates.append(value)
        seen.append(value)
    return duplicates

data = [1, 2, 1, 3, 2, 4, 5, 4]
print(remove_duplicates(data))
print(count_duplicates(data))
print(has_duplicates(data))
print(get_duplicates(data))
