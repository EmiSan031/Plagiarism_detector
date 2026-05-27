def rotate_left(items, steps):
    steps = steps % len(items)
    return items[steps:] + items[:steps]

def rotate_right(items, steps):
    steps = steps % len(items)
    return items[-steps:] + items[:-steps]

def rotate_all(items):
    return [rotate_left(items, k) for k in range(len(items))]

def is_rotation(a, b):
    return len(a) == len(b) and b in rotate_all(a)

data = [1, 2, 3, 4, 5]
print(rotate_left(data, 2))
print(rotate_right(data, 2))
print(is_rotation(data, [3, 4, 5, 1, 2]))
print(is_rotation(data, [3, 4, 5, 2, 1]))
