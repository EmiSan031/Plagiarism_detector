def bubble_sort(values):
    items = values[:]
    for i in range(len(items)):
        for j in range(0, len(items) - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

def is_sorted(values):
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            return False
    return True

def sort_report(values):
    print(f"Original        : {values}")
    print(f"Already sorted  : {is_sorted(values)}")
    sorted_list = bubble_sort(values)
    print(f"Sorted          : {sorted_list}")
    print(f"Verified sorted : {is_sorted(sorted_list)}")
    total = 0
    for v in sorted_list:
        total += v
    count = len(sorted_list)
    print(f"Smallest        : {sorted_list[0]}")
    print(f"Largest         : {sorted_list[-1]}")
    print(f"Sum             : {total}")
    print(f"Average         : {total / count:.2f}")

sort_report([5, 1, 4, 2, 8])
