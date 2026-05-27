# Type I clone: only comments and whitespace differ.

def total_plants(plants):
    total = 0
    for item in plants:
        total += item["height"]
    return total


# Same function body as the original fragment.
def average_plants(plants):
    if not plants:
        return 0
    return total_plants(plants) / len(plants)


# Same function body as the original fragment.
def count_high_plants(plants, minimum):
    count = 0
    for item in plants:
        if item["height"] >= minimum:
            count += 1
    return count


# Same function body as the original fragment.
def plant_report(plants, minimum):
    total = total_plants(plants)
    average = average_plants(plants)
    high_count = count_high_plants(plants, minimum)
    print(f"Total height: {total}")
    print(f"Average height: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_plants = [{"name": "basil", "height": 18}, {"name": "mint", "height": 12}, {"name": "rose", "height": 31}]
plant_report(records_plants, 10)
