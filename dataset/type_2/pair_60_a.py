def total_supplies(boxes):
    total = 0
    for item in boxes:
        total += item["items"]
    return total

def average_supplies(boxes):
    if not boxes:
        return 0
    return total_supplies(boxes) / len(boxes)

def count_high_supplies(boxes, minimum):
    count = 0
    for item in boxes:
        if item["items"] >= minimum:
            count += 1
    return count

def supply_report(boxes, minimum):
    total = total_supplies(boxes)
    average = average_supplies(boxes)
    high_count = count_high_supplies(boxes, minimum)
    print(f"Total items: {total}")
    print(f"Average items: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_supplies = [{"box": "red", "items": 15}, {"box": "blue", "items": 22}, {"box": "green", "items": 11}]
supply_report(records_supplies, 10)
