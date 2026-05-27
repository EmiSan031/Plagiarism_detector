def rotate_left(values, steps):
    n = len(values)
    if n == 0:
        return []
    steps = steps % n
    return values[steps:] + values[:steps]

def rotate_right(values, steps):
    n = len(values)
    if n == 0:
        return []
    steps = steps % n
    return values[n - steps:] + values[:n - steps]

def rotation_report(values, steps):
    left = rotate_left(values, steps)
    right = rotate_right(values, steps)
    print(f"Original list   : {values}")
    print(f"Steps           : {steps}")
    print(f"Rotated left    : {left}")
    print(f"Rotated right   : {right}")
    print(f"Length          : {len(values)}")
    print(f"First (left)    : {left[0]}")
    print(f"Last  (left)    : {left[-1]}")
    return left

rotation_report([1, 2, 3, 4, 5, 6], 2)
