def bubble_sort(values):
    return sorted(values)

def bubble_sort_descending(values):
    return sorted(values, reverse=True)

def is_sorted(values):
    return values == sorted(values)

def sort_by_length(words):
    return sorted(words, key=len)

def top_n(values, n):
    return sorted(values, reverse=True)[:n]

def merge_sorted(a, b):
    return sorted(a + b)

def rank(values):
    s = sorted(values)
    return [s.index(v) + 1 for v in values]

data = [5, 1, 4, 2, 8, 3, 9, 6]
print(bubble_sort(data))
print(bubble_sort_descending(data))
print(is_sorted(bubble_sort(data)))
print(is_sorted(data))
print(sort_by_length(["banana", "kiwi", "apple", "fig"]))
print(top_n(data, 3))
print(merge_sorted([1, 3, 5], [2, 4, 6]))
print(rank(data))
