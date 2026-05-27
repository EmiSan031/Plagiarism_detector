def total_bakery(batches):
    total = 0
    for item in batches:
        total += item["loaves"]
    return total

def average_bakery(batches):
    if not batches:
        return 0
    return total_bakery(batches) / len(batches)

def high_bakery(batches, minimum):
    selected = []
    for item in batches:
        if item["loaves"] >= minimum:
            selected.append(item)
    return selected

def bakery_report(batches, minimum):
    total = total_bakery(batches)
    average = average_bakery(batches)
    selected = high_bakery(batches, minimum)
    print(f"Records         : {batches}")
    print(f"Total loaves  : {total}")
    print(f"Average loaves: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_bakery = [{"batch": "morning", "loaves": 80, "defects": 3}, {"batch": "noon", "loaves": 65, "defects": 1}]
bakery_report(example_bakery, 10)
