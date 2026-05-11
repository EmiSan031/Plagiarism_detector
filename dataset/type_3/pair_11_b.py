def locate_sorted(data, goal):
    if not data:
        return -1
    low = 0
    high = len(data) - 1
    attempts = 0
    while low <= high:
        attempts += 1
        center = (low + high) // 2
        if data[center] == goal:
            return center
        if data[center] < goal:
            low = center + 1
        else:
            high = center - 1
    print("attempts:", attempts)
    return -1


print(locate_sorted([1, 4, 7, 10, 13], 10))
