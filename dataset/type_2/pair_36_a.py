def total_races(runners):
    total = 0
    for item in runners:
        total += item["seconds"]
    return total

def average_races(runners):
    if not runners:
        return 0
    return total_races(runners) / len(runners)

def count_high_races(runners, minimum):
    count = 0
    for item in runners:
        if item["seconds"] >= minimum:
            count += 1
    return count

def race_report(runners, minimum):
    total = total_races(runners)
    average = average_races(runners)
    high_count = count_high_races(runners, minimum)
    print(f"Total seconds: {total}")
    print(f"Average seconds: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_races = [{"runner": "A", "seconds": 64}, {"runner": "B", "seconds": 59}, {"runner": "C", "seconds": 72}]
race_report(records_races, 10)
