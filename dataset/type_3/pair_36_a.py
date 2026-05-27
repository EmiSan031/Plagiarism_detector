def sort_list(values):
    items = values[:]
    for i in range(len(items)):
        for j in range(0, len(items) - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

def median(values):
    sorted_vals = sort_list(values)
    n = len(sorted_vals)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
    return sorted_vals[mid]

def median_report(values):
    result = median(values)
    sorted_vals = sort_list(values)
    total = 0
    for v in values:
        total += v
    print(f"Original list   : {values}")
    print(f"Sorted list     : {sorted_vals}")
    print(f"Count           : {len(values)}")
    print(f"Median          : {result}")
    print(f"Mean            : {total / len(values):.2f}")
    print(f"Min             : {sorted_vals[0]}")
    print(f"Max             : {sorted_vals[-1]}")
    return result

median_report([7, 2, 10, 9, 3, 6, 1])
