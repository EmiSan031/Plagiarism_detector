def insertion_sort(values):
    items = values[:]
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0 and items[j] > key:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key
    return items

def n_smallest(values, n):
    sorted_vals = insertion_sort(values)
    return sorted_vals[:n]

def n_largest(values, n):
    sorted_vals = insertion_sort(values)
    return sorted_vals[-n:]

def median(values):
    sorted_vals = insertion_sort(values)
    mid = len(sorted_vals) // 2
    if len(sorted_vals) % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
    return sorted_vals[mid]

data = [5, 2, 8, 1, 9, 3, 7, 4, 6]
print(insertion_sort(data))
print(n_smallest(data, 3))
print(n_largest(data, 3))
print(median(data))
