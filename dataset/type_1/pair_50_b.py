# Type I clone: only comments and whitespace differ.

def total_fuel(fills):
    total = 0
    for item in fills:
        total += item["liters"]
    return total


# Same function body as the original fragment.
def average_fuel(fills):
    if not fills:
        return 0
    return total_fuel(fills) / len(fills)


# Same function body as the original fragment.
def count_high_fuel(fills, minimum):
    count = 0
    for item in fills:
        if item["liters"] >= minimum:
            count += 1
    return count


# Same function body as the original fragment.
def fuel_report(fills, minimum):
    total = total_fuel(fills)
    average = average_fuel(fills)
    high_count = count_high_fuel(fills, minimum)
    print(f"Total liters: {total}")
    print(f"Average liters: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_fuel = [{"station": "A", "liters": 30}, {"station": "B", "liters": 22}, {"station": "C", "liters": 40}]
fuel_report(records_fuel, 10)
