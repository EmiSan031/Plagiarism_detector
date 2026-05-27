# Type I clone: only comments and whitespace differ.

def total_trips(trips):
    total = 0
    for item in trips:
        total += item["days"]
    return total


# Same function body as the original fragment.
def average_trips(trips):
    if not trips:
        return 0
    return total_trips(trips) / len(trips)


# Same function body as the original fragment.
def count_high_trips(trips, minimum):
    count = 0
    for item in trips:
        if item["days"] >= minimum:
            count += 1
    return count


# Same function body as the original fragment.
def trip_report(trips, minimum):
    total = total_trips(trips)
    average = average_trips(trips)
    high_count = count_high_trips(trips, minimum)
    print(f"Total days: {total}")
    print(f"Average days: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_trips = [{"city": "A", "days": 3}, {"city": "B", "days": 5}, {"city": "C", "days": 2}]
trip_report(records_trips, 10)
