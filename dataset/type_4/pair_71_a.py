def total_files(files):
    result = 0
    for item in files:
        result = result + item["bytes"]
    return result

def average_files(files):
    count = 0
    total = 0
    for item in files:
        count += 1
        total += item["bytes"]
    if count == 0:
        return 0
    return total / count

def maximum_files(files):
    if not files:
        return None
    best = files[0]
    for item in files[1:]:
        if item["bytes"] > best["bytes"]:
            best = item
    return best

def select_files(files, minimum):
    selected = []
    for item in files:
        if item["bytes"] >= minimum:
            selected.append(item)
    return selected

def file_report(files, minimum):
    total = total_files(files)
    average = average_files(files)
    best = maximum_files(files)
    selected = select_files(files, minimum)
    print(f"Total bytes: {total}")
    print(f"Average bytes: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_files = [{"path": "a.txt", "bytes": 1200}, {"path": "b.log", "bytes": 5400}, {"path": "c.csv", "bytes": 900}]
file_report(data_files, 10)
