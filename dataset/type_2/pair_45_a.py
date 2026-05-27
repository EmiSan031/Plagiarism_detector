def total_downloads(files):
    total = 0
    for item in files:
        total += item["downloads"]
    return total

def average_downloads(files):
    if not files:
        return 0
    return total_downloads(files) / len(files)

def count_high_downloads(files, minimum):
    count = 0
    for item in files:
        if item["downloads"] >= minimum:
            count += 1
    return count

def download_report(files, minimum):
    total = total_downloads(files)
    average = average_downloads(files)
    high_count = count_high_downloads(files, minimum)
    print(f"Total downloads: {total}")
    print(f"Average downloads: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_downloads = [{"file": "app", "downloads": 120}, {"file": "doc", "downloads": 42}, {"file": "img", "downloads": 75}]
download_report(records_downloads, 10)
