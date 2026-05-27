def total_pets(pets):
    total = 0
    for item in pets:
        total += item["weight"]
    return total

def average_pets(pets):
    if not pets:
        return 0
    return total_pets(pets) / len(pets)

def count_high_pets(pets, minimum):
    count = 0
    for item in pets:
        if item["weight"] >= minimum:
            count += 1
    return count

def pet_report(pets, minimum):
    total = total_pets(pets)
    average = average_pets(pets)
    high_count = count_high_pets(pets, minimum)
    print(f"Total weight: {total}")
    print(f"Average weight: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_pets = [{"name": "Luna", "weight": 8}, {"name": "Max", "weight": 12}, {"name": "Nox", "weight": 5}]
pet_report(records_pets, 10)
