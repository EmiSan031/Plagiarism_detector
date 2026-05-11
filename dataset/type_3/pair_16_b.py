def unique_items(sequence):
    clean = []
    repeated = 0
    for element in sequence:
        if element not in clean:
            clean.append(element)
        else:
            repeated += 1
    print("duplicates:", repeated)
    return clean


print(unique_items([1, 2, 1, 3, 2, 4]))
