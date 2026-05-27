def total_library(loans):
    result = 0
    for item in loans:
        result = result + item["days_late"]
    return result

def average_library(loans):
    count = 0
    total = 0
    for item in loans:
        count += 1
        total += item["days_late"]
    if count == 0:
        return 0
    return total / count

def maximum_library(loans):
    if not loans:
        return None
    best = loans[0]
    for item in loans[1:]:
        if item["days_late"] > best["days_late"]:
            best = item
    return best

def select_library(loans, minimum):
    selected = []
    for item in loans:
        if item["days_late"] >= minimum:
            selected.append(item)
    return selected

def library_report(loans, minimum):
    total = total_library(loans)
    average = average_library(loans)
    best = maximum_library(loans)
    selected = select_library(loans, minimum)
    print(f"Total days_late: {total}")
    print(f"Average days_late: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_library = [{"book": "A", "days_late": 2}, {"book": "B", "days_late": 0}, {"book": "C", "days_late": 5}]
library_report(data_library, 10)
