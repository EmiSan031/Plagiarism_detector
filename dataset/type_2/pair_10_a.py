def linear_search(values, target):
    for index in range(len(values)):
        if values[index] == target:
            return index
    return -1

def count_occurrences(values, target):
    count = 0
    for value in values:
        if value == target:
            count += 1
    return count

def search_report(values, target):
    position = linear_search(values, target)
    occurrences = count_occurrences(values, target)
    print(f"List            : {values}")
    print(f"Search target   : {target}")
    print(f"List length     : {len(values)}")
    if position != -1:
        print(f"Target found at index: {position}")
        print(f"Value at index  : {values[position]}")
    else:
        print(f"Target {target} was NOT found in the list.")
    print(f"Total occurrences: {occurrences}")
    for i, val in enumerate(values):
        status = "<-- found" if val == target else ""
        print(f"  index {i}: {val} {status}")

search_report([3, 6, 9, 12], 9)
