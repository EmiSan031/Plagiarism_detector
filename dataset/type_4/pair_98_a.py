def total_bakery(batches):
    result = 0
    for item in batches:
        result = result + item["loaves"]
    return result

def average_bakery(batches):
    count = 0
    total = 0
    for item in batches:
        count += 1
        total += item["loaves"]
    if count == 0:
        return 0
    return total / count

def maximum_bakery(batches):
    if not batches:
        return None
    best = batches[0]
    for item in batches[1:]:
        if item["loaves"] > best["loaves"]:
            best = item
    return best

def select_bakery(batches, minimum):
    selected = []
    for item in batches:
        if item["loaves"] >= minimum:
            selected.append(item)
    return selected

def bakery_report(batches, minimum):
    total = total_bakery(batches)
    average = average_bakery(batches)
    best = maximum_bakery(batches)
    selected = select_bakery(batches, minimum)
    print(f"Total loaves: {total}")
    print(f"Average loaves: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_bakery = [{"batch": "morning", "loaves": 80}, {"batch": "noon", "loaves": 65}, {"batch": "night", "loaves": 72}]
bakery_report(data_bakery, 10)
