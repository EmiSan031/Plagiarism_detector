def interleave(a, b):
    result = []
    length = min(len(a), len(b))
    for i in range(length):
        result.append(a[i])
        result.append(b[i])
    for item in a[length:]:
        result.append(item)
    for item in b[length:]:
        result.append(item)
    return result

def split_in_half(items):
    mid = len(items) // 2
    first = []
    second = []
    for i in range(mid):
        first.append(items[i])
    for i in range(mid, len(items)):
        second.append(items[i])
    return first, second

def chunk(items, size):
    result = []
    i = 0
    while i < len(items):
        group = []
        for j in range(size):
            if i + j < len(items):
                group.append(items[i + j])
        result.append(group)
        i += size
    return result

data = [1, 2, 3, 4, 5, 6, 7, 8]
print(interleave([1, 3, 5], [2, 4, 6]))
print(split_in_half(data))
print(chunk(data, 3))
