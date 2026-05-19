def binary_search(values, target):
    left = 0
    right = len(values) - 1
    steps = 0
    while left <= right:
        middle = (left + right) // 2
        steps += 1
        if values[middle] == target:
            return middle, steps
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1, steps

def search_report(values, target):
    if not values:
        print("The list is empty, cannot perform search.")
        return
    print(f"Sorted list     : {values}")
    print(f"Search target   : {target}")
    print(f"List length     : {len(values)}")
    position, steps = binary_search(values, target)
    print(f"Steps taken     : {steps}")
    if position != -1:
        print(f"Target found at index: {position}")
        print(f"Value at index  : {values[position]}")
    else:
        print(f"Target {target} was NOT found in the list.")
    print(f"Minimum value   : {values[0]}")
    print(f"Maximum value   : {values[-1]}")

search_report([1, 4, 7, 10, 13], 10)
print()
search_report([1, 4, 7, 10, 13], 5)
