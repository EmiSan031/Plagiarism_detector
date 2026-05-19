def bubble_sort(values):
    items = values[:]
    for i in range(len(items)):
        for j in range(0, len(items) - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

def count_swaps(values):
    items = values[:]
    swaps = 0
    for i in range(len(items)):
        for j in range(0, len(items) - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swaps += 1
    return swaps

def sort_report(values):
    sorted_list = bubble_sort(values)
    swaps = count_swaps(values)
    print(f"Original list   : {values}")
    print(f"Sorted list     : {sorted_list}")
    print(f"Total swaps     : {swaps}")
    print(f"Smallest element: {sorted_list[0]}")
    print(f"Largest element : {sorted_list[-1]}")
    count = len(sorted_list)
    total = sum(sorted_list)
    print(f"Element count   : {count}")
    print(f"Sum of elements : {total}")
    print(f"Average value   : {total / count:.2f}")

sort_report([5, 1, 4, 2, 8])
