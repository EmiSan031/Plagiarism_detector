def arrange(data):
    copy = data[:]
    for outer in range(len(copy)):
        for inner in range(0, len(copy) - outer - 1):
            if copy[inner] > copy[inner + 1]:
                copy[inner], copy[inner + 1] = copy[inner + 1], copy[inner]
    return copy

def find_median(data):
    if len(data) == 0:
        return None
    arranged = arrange(data)
    size = len(arranged)
    center = size // 2
    if size % 2 == 0:
        return (arranged[center - 1] + arranged[center]) / 2
    return arranged[center]

def find_mode(data):
    freq = {}
    for item in data:
        if item not in freq:
            freq[item] = 0
        freq[item] += 1
    peak = 0
    mode = data[0]
    for item in freq:
        if freq[item] > peak:
            peak = freq[item]
            mode = item
    return mode

def stats_report(data):
    if len(data) == 0:
        print("Dataset is empty.")
        return None
    mid = find_median(data)
    mode = find_mode(data)
    arranged = arrange(data)
    grand_total = sum(data)
    print(f"Original data   : {data}")
    print(f"Count           : {len(data)}")
    print(f"Median          : {mid}")
    print(f"Mode            : {mode}")
    print(f"Mean            : {grand_total / len(data):.2f}")
    print(f"Min / Max       : {arranged[0]} / {arranged[-1]}")
    return mid

stats_report([7, 2, 10, 9, 3, 6, 1])
