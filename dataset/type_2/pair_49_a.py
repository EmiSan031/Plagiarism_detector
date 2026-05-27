def total_printing(jobs):
    total = 0
    for item in jobs:
        total += item["pages"]
    return total

def average_printing(jobs):
    if not jobs:
        return 0
    return total_printing(jobs) / len(jobs)

def count_high_printing(jobs, minimum):
    count = 0
    for item in jobs:
        if item["pages"] >= minimum:
            count += 1
    return count

def print_report(jobs, minimum):
    total = total_printing(jobs)
    average = average_printing(jobs)
    high_count = count_high_printing(jobs, minimum)
    print(f"Total pages: {total}")
    print(f"Average pages: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_printing = [{"job": "a", "pages": 10}, {"job": "b", "pages": 25}, {"job": "c", "pages": 6}]
print_report(records_printing, 10)
