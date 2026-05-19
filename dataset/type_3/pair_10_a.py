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
    print(f"Target          : {target}")
    print(f"List size       : {len(values)}")
    if position != -1:
        print(f"Found at index  : {position}")
    else:
        print(f"Target not found in list.")
    print(f"Occurrences     : {occurrences}")
    for i, val in enumerate(values):
        marker = " <-- found" if val == target else ""
        print(f"  [{i}] {val}{marker}")

search_report([3, 6, 9, 12], 9)
