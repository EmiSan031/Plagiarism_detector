def total_laundry(loads):
    total = 0
    for item in loads:
        total += item["pounds"]
    return total

def average_laundry(loads):
    if not loads:
        return 0
    return total_laundry(loads) / len(loads)

def count_high_laundry(loads, minimum):
    count = 0
    for item in loads:
        if item["pounds"] >= minimum:
            count += 1
    return count

def laundry_report(loads, minimum):
    total = total_laundry(loads)
    average = average_laundry(loads)
    high_count = count_high_laundry(loads, minimum)
    print(f"Total pounds: {total}")
    print(f"Average pounds: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_laundry = [{"load": "white", "pounds": 9}, {"load": "color", "pounds": 12}, {"load": "linen", "pounds": 7}]
laundry_report(records_laundry, 10)
