def intersection(a, b):
    return sorted(set(a) & set(b))

def union(a, b):
    return sorted(set(a) | set(b))

def difference(a, b):
    return sorted(set(a) - set(b))

def is_subset(a, b):
    return set(a).issubset(set(b))

x = [1, 2, 3, 4, 5]
y = [3, 4, 5, 6, 7]
print(intersection(x, y))
print(union(x, y))
print(difference(x, y))
print(is_subset([3, 4], x))
print(is_subset([3, 9], x))
