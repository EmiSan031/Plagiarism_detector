def find_duplicates(values):
    seen = set()
    duplicates = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return sorted(duplicates)

print(find_duplicates([1, 2, 2, 3, 4, 4]))
