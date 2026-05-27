# Type I clone: only comments and whitespace differ.

def total_deliveries(drops):
    total = 0
    for item in drops:
        total += item["miles"]
    return total


# Same function body as the original fragment.
def average_deliveries(drops):
    if not drops:
        return 0
    return total_deliveries(drops) / len(drops)


# Same function body as the original fragment.
def count_high_deliveries(drops, minimum):
    count = 0
    for item in drops:
        if item["miles"] >= minimum:
            count += 1
    return count


# Same function body as the original fragment.
def delivery_report(drops, minimum):
    total = total_deliveries(drops)
    average = average_deliveries(drops)
    high_count = count_high_deliveries(drops, minimum)
    print(f"Total miles: {total}")
    print(f"Average miles: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_deliveries = [{"code": "D1", "miles": 14}, {"code": "D2", "miles": 8}, {"code": "D3", "miles": 19}]
delivery_report(records_deliveries, 10)
