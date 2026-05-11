# Keep the first occurrence only.
def remove_duplicates(values):
    result = []

    for value in values:
        if value not in result:
            result.append(value)
    return result


print(remove_duplicates([1, 2, 1, 3, 2, 4]))
