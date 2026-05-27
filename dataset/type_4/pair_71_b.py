def total_files(files):
    return sum(map(lambda entry: entry["bytes"], files))

def average_files(files):
    values = tuple(entry["bytes"] for entry in files)
    return sum(values) / len(values) if values else 0

def maximum_files(files):
    return max(files, key=lambda entry: entry["bytes"], default=None)

def select_files(files, minimum):
    return list(filter(lambda entry: entry["bytes"] >= minimum, files))

def file_report(files, minimum):
    summary = (
        total_files(files),
        average_files(files),
        maximum_files(files),
        select_files(files, minimum),
    )
    labels = ("Total bytes", "Average bytes", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_files = [{"path": "a.txt", "bytes": 1200}, {"path": "b.log", "bytes": 5400}, {"path": "c.csv", "bytes": 900}]
file_report(data_files, 10)
