def total_files(files):
    total = 0
    for item in files:
        total += item["bytes"]
    return total

def average_files(files):
    if not files:
        return 0
    return total_files(files) / len(files)

def high_files(files, minimum):
    selected = []
    for item in files:
        if item["bytes"] >= minimum:
            selected.append(item)
    return selected

def file_report(files, minimum):
    total = total_files(files)
    average = average_files(files)
    selected = high_files(files, minimum)
    print(f"Records         : {files}")
    print(f"Total bytes  : {total}")
    print(f"Average bytes: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_files = [{"path": "a.txt", "bytes": 1200, "age": 4}, {"path": "b.log", "bytes": 5400, "age": 12}]
file_report(example_files, 10)
