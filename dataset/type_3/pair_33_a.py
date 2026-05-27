def is_sorted(values):
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            return False
    return True

def first_unsorted_index(values):
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            return i
    return -1

def sorted_report(values):
    result = is_sorted(values)
    idx = first_unsorted_index(values)
    print(f"List            : {values}")
    print(f"Length          : {len(values)}")
    print(f"Is sorted       : {result}")
    if not result:
        print(f"First break at  : index {idx} (value {values[idx]})")
    else:
        print(f"All elements in ascending order.")
    print(f"Min value       : {values[0] if result else '?'}")
    print(f"Max value       : {values[-1] if result else '?'}")
    return result

sorted_report([1, 3, 5, 7, 9])
print()
sorted_report([1, 5, 3, 7, 9])
