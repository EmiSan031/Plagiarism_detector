# Type I clone: only comments and whitespace differ.

def total_calls(calls):
    total = 0
    for item in calls:
        total += item["minutes"]
    return total


# Same function body as the original fragment.
def average_calls(calls):
    if not calls:
        return 0
    return total_calls(calls) / len(calls)


# Same function body as the original fragment.
def count_high_calls(calls, minimum):
    count = 0
    for item in calls:
        if item["minutes"] >= minimum:
            count += 1
    return count


# Same function body as the original fragment.
def call_report(calls, minimum):
    total = total_calls(calls)
    average = average_calls(calls)
    high_count = count_high_calls(calls, minimum)
    print(f"Total minutes: {total}")
    print(f"Average minutes: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_calls = [{"number": "111", "minutes": 5}, {"number": "222", "minutes": 11}, {"number": "333", "minutes": 2}]
call_report(records_calls, 10)
