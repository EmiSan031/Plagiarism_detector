def selection_sort(values):
    items = values[:]
    for i in range(len(items)):
        min_index = i
        for j in range(i + 1, len(items)):
            if items[j] < items[min_index]:
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

def sort_by_absolute(values):
    items = values[:]
    for i in range(len(items)):
        min_index = i
        for j in range(i + 1, len(items)):
            if abs(items[j]) < abs(items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

def sort_strings_by_length(words):
    items = words[:]
    for i in range(len(items)):
        min_index = i
        for j in range(i + 1, len(items)):
            if len(items[j]) < len(items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

print(selection_sort([64, 25, 12, 22, 11]))
print(sort_by_absolute([-5, 3, -1, 4, -2]))
print(sort_strings_by_length(["banana", "kiwi", "apple", "fig", "mango"]))
