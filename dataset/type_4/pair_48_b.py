def selection_sort(values):
    return sorted(values)

def sort_by_absolute(values):
    return sorted(values, key=abs)

def sort_strings_by_length(words):
    return sorted(words, key=len)

def sort_by_last_char(words):
    return sorted(words, key=lambda w: w[-1])

def sort_descending(values):
    return sorted(values, reverse=True)

def stable_sort_multi(data, key1, key2):
    return sorted(data, key=lambda x: (x[key1], x[key2]))

print(selection_sort([64, 25, 12, 22, 11]))
print(sort_by_absolute([-5, 3, -1, 4, -2]))
print(sort_strings_by_length(["banana", "kiwi", "apple", "fig", "mango"]))
print(sort_by_last_char(["banana", "kiwi", "apple"]))
print(sort_descending([3, 1, 4, 1, 5, 9]))
