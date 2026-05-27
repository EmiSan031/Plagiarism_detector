def total_storage(drives):
    total = 0
    for item in drives:
        total += item["gigabytes"]
    return total

def average_storage(drives):
    if not drives:
        return 0
    return total_storage(drives) / len(drives)

def count_high_storage(drives, minimum):
    count = 0
    for item in drives:
        if item["gigabytes"] >= minimum:
            count += 1
    return count

def storage_report(drives, minimum):
    total = total_storage(drives)
    average = average_storage(drives)
    high_count = count_high_storage(drives, minimum)
    print(f"Total gigabytes: {total}")
    print(f"Average gigabytes: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_storage = [{"drive": "A", "gigabytes": 512}, {"drive": "B", "gigabytes": 256}, {"drive": "C", "gigabytes": 1024}]
storage_report(records_storage, 10)
