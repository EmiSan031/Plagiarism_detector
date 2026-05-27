def intersection(a, b):
    result = []
    for item in a:
        if item in b and item not in result:
            result.append(item)
    return result

def union(a, b):
    result = []
    for item in a:
        if item not in result:
            result.append(item)
    for item in b:
        if item not in result:
            result.append(item)
    return result

def difference(a, b):
    result = []
    for item in a:
        if item not in b:
            result.append(item)
    return result

def is_subset(a, b):
    for item in a:
        if item not in b:
            return False
    return True

x = [1, 2, 3, 4, 5]
y = [3, 4, 5, 6, 7]
print(sorted(intersection(x, y)))
print(sorted(union(x, y)))
print(sorted(difference(x, y)))
print(is_subset([3, 4], x))
print(is_subset([3, 9], x))
