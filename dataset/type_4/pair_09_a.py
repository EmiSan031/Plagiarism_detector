def bubble_sort(values):
    items = values[:]
    for i in range(len(items)):
        for j in range(0, len(items) - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

def bubble_sort_descending(values):
    items = values[:]
    for i in range(len(items)):
        for j in range(0, len(items) - i - 1):
            if items[j] < items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

def is_sorted(values):
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            return False
    return True

data = [5, 1, 4, 2, 8, 3, 9, 6]
print(bubble_sort(data))
print(bubble_sort_descending(data))
print(is_sorted(bubble_sort(data)))
print(is_sorted(data))
