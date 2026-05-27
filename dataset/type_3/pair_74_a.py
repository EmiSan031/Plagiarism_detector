def total_library(loans):
    total = 0
    for item in loans:
        total += item["days_late"]
    return total

def average_library(loans):
    if not loans:
        return 0
    return total_library(loans) / len(loans)

def high_library(loans, minimum):
    selected = []
    for item in loans:
        if item["days_late"] >= minimum:
            selected.append(item)
    return selected

def library_report(loans, minimum):
    total = total_library(loans)
    average = average_library(loans)
    selected = high_library(loans, minimum)
    print(f"Records         : {loans}")
    print(f"Total days_late  : {total}")
    print(f"Average days_late: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_library = [{"book": "A", "days_late": 2, "daily_fee": 3}, {"book": "B", "days_late": 0, "daily_fee": 3}]
library_report(example_library, 10)
