def remove_duplicates(values):
    return list(dict.fromkeys(values))


print(remove_duplicates([1, 2, 1, 3, 2, 4]))
