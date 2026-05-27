# Type I clone: only comments and whitespace differ.

def total_mileage(cars):
    total = 0
    for item in cars:
        total += item["kilometers"]
    return total


# Same function body as the original fragment.
def average_mileage(cars):
    if not cars:
        return 0
    return total_mileage(cars) / len(cars)


# Same function body as the original fragment.
def count_high_mileage(cars, minimum):
    count = 0
    for item in cars:
        if item["kilometers"] >= minimum:
            count += 1
    return count


# Same function body as the original fragment.
def mileage_report(cars, minimum):
    total = total_mileage(cars)
    average = average_mileage(cars)
    high_count = count_high_mileage(cars, minimum)
    print(f"Total kilometers: {total}")
    print(f"Average kilometers: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_mileage = [{"car": "sedan", "kilometers": 240}, {"car": "van", "kilometers": 180}, {"car": "truck", "kilometers": 310}]
mileage_report(records_mileage, 10)
