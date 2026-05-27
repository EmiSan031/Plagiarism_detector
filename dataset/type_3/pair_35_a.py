def interleave(list_a, list_b):
    result = []
    length = min(len(list_a), len(list_b))
    for i in range(length):
        result.append(list_a[i])
        result.append(list_b[i])
    for item in list_a[length:]:
        result.append(item)
    for item in list_b[length:]:
        result.append(item)
    return result

def interleave_report(list_a, list_b):
    merged = interleave(list_a, list_b)
    print(f"List A          : {list_a}")
    print(f"List B          : {list_b}")
    print(f"Interleaved     : {merged}")
    print(f"Total elements  : {len(merged)}")
    total = 0
    for v in merged:
        total += v
    print(f"Sum of merged   : {total}")
    print(f"First element   : {merged[0]}")
    print(f"Last element    : {merged[-1]}")
    return merged

interleave_report([1, 3, 5, 7], [2, 4, 6, 8])
