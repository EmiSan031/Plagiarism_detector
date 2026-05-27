def total_library(loans):
    return sum(map(lambda entry: entry["days_late"], loans))

def average_library(loans):
    values = tuple(entry["days_late"] for entry in loans)
    return sum(values) / len(values) if values else 0

def maximum_library(loans):
    return max(loans, key=lambda entry: entry["days_late"], default=None)

def select_library(loans, minimum):
    return list(filter(lambda entry: entry["days_late"] >= minimum, loans))

def library_report(loans, minimum):
    summary = (
        total_library(loans),
        average_library(loans),
        maximum_library(loans),
        select_library(loans, minimum),
    )
    labels = ("Total days_late", "Average days_late", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_library = [{"book": "A", "days_late": 2}, {"book": "B", "days_late": 0}, {"book": "C", "days_late": 5}]
library_report(data_library, 10)
