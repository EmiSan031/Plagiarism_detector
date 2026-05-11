def locate_sorted(data, goal):
    low = 0
    high = len(data) - 1
    while low <= high:
        center = (low + high) // 2
        if data[center] == goal:
            return center
        if data[center] < goal:
            low = center + 1
        else:
            high = center - 1
    return -1


print(locate_sorted([2, 5, 8, 11, 14], 11))
