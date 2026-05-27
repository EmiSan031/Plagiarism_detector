# Type I clone: only comments and whitespace differ.

def total_repairs(tickets):
    total = 0
    for item in tickets:
        total += item["cost"]
    return total


# Same function body as the original fragment.
def average_repairs(tickets):
    if not tickets:
        return 0
    return total_repairs(tickets) / len(tickets)


# Same function body as the original fragment.
def count_high_repairs(tickets, minimum):
    count = 0
    for item in tickets:
        if item["cost"] >= minimum:
            count += 1
    return count


# Same function body as the original fragment.
def repair_report(tickets, minimum):
    total = total_repairs(tickets)
    average = average_repairs(tickets)
    high_count = count_high_repairs(tickets, minimum)
    print(f"Total cost: {total}")
    print(f"Average cost: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_repairs = [{"id": "R1", "cost": 45}, {"id": "R2", "cost": 80}, {"id": "R3", "cost": 25}]
repair_report(records_repairs, 10)
