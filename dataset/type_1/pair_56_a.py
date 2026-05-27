def total_coffee(cups):
    total = 0
    for item in cups:
        total += item["ounces"]
    return total

def average_coffee(cups):
    if not cups:
        return 0
    return total_coffee(cups) / len(cups)

def count_high_coffee(cups, minimum):
    count = 0
    for item in cups:
        if item["ounces"] >= minimum:
            count += 1
    return count

def coffee_report(cups, minimum):
    total = total_coffee(cups)
    average = average_coffee(cups)
    high_count = count_high_coffee(cups, minimum)
    print(f"Total ounces: {total}")
    print(f"Average ounces: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_coffee = [{"drink": "latte", "ounces": 12}, {"drink": "mocha", "ounces": 16}, {"drink": "tea", "ounces": 10}]
coffee_report(records_coffee, 10)
