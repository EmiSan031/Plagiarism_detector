def rotate_left(items, steps):
    n = len(items)
    steps = steps % n
    result = []
    for i in range(steps, n):
        result.append(items[i])
    for i in range(steps):
        result.append(items[i])
    return result

def rotate_right(items, steps):
    return rotate_left(items, len(items) - steps % len(items))

def rotate_all(items):
    rotations = []
    for k in range(len(items)):
        rotations.append(rotate_left(items, k))
    return rotations

def is_rotation(a, b):
    if len(a) != len(b):
        return False
    for rotation in rotate_all(a):
        if rotation == b:
            return True
    return False

data = [1, 2, 3, 4, 5]
print(rotate_left(data, 2))
print(rotate_right(data, 2))
print(is_rotation(data, [3, 4, 5, 1, 2]))
print(is_rotation(data, [3, 4, 5, 2, 1]))
