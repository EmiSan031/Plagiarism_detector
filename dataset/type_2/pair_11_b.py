def locate_sorted(data, goal):
    low = 0
    high = len(data) - 1
    attempts = 0
    while low <= high:
        center = (low + high) // 2
        attempts += 1
        if data[center] == goal:
            return center, attempts
        if data[center] < goal:
            low = center + 1
        else:
            high = center - 1
    return -1, attempts

def lookup_report(data, goal):
    if not data:
        print("The dataset is empty, search aborted.")
        return
    print(f"Dataset         : {data}")
    print(f"Goal value      : {goal}")
    print(f"Dataset size    : {len(data)}")
    location, attempts = locate_sorted(data, goal)
    print(f"Attempts made   : {attempts}")
    if location != -1:
        print(f"Goal found at index: {location}")
        print(f"Stored value    : {data[location]}")
    else:
        print(f"Goal {goal} was NOT found in the dataset.")
    print(f"Lowest entry    : {data[0]}")
    print(f"Highest entry   : {data[-1]}")

lookup_report([2, 5, 8, 11, 14], 11)
print()
lookup_report([2, 5, 8, 11, 14], 6)
