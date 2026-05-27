def total_garden(beds):
    total = 0
    for item in beds:
        total += item["plants"]
    return total

def average_garden(beds):
    if not beds:
        return 0
    return total_garden(beds) / len(beds)

def count_high_garden(beds, minimum):
    count = 0
    for item in beds:
        if item["plants"] >= minimum:
            count += 1
    return count

def garden_report(beds, minimum):
    total = total_garden(beds)
    average = average_garden(beds)
    high_count = count_high_garden(beds, minimum)
    print(f"Total plants: {total}")
    print(f"Average plants: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_garden = [{"bed": "A", "plants": 18}, {"bed": "B", "plants": 24}, {"bed": "C", "plants": 15}]
garden_report(records_garden, 10)
