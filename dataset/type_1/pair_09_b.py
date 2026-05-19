def bubble_sort(values):
    items = values[:]

    for i in range(len(items)):
        for j in range(0, len(items) - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]

    return items

# Returns True if the list is in ascending order.
def is_sorted(values):
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            return False
    return True

def bubble_sort_descending(values):
    items = values[:]
    for i in range(len(items)):
        for j in range(0, len(items) - i - 1):
            if items[j] < items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

# Sorting example.
data = [5, 1, 4, 2, 8, 3, 9, 6]
sorted_asc = bubble_sort(data)
sorted_desc = bubble_sort_descending(data)
print(sorted_asc)
print(sorted_desc)
print(is_sorted(sorted_asc))
print(is_sorted(data))
