def unique_items(sequence):
    clean = []
    for element in sequence:
        if element not in clean:
            clean.append(element)
    return clean


print(unique_items([5, 6, 5, 7, 6, 8]))
