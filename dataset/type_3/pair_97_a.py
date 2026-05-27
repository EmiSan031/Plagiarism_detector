def total_rentals(cars):
    total = 0
    for item in cars:
        total += item["days"]
    return total

def average_rentals(cars):
    if not cars:
        return 0
    return total_rentals(cars) / len(cars)

def high_rentals(cars, minimum):
    selected = []
    for item in cars:
        if item["days"] >= minimum:
            selected.append(item)
    return selected

def rental_report(cars, minimum):
    total = total_rentals(cars)
    average = average_rentals(cars)
    selected = high_rentals(cars, minimum)
    print(f"Records         : {cars}")
    print(f"Total days  : {total}")
    print(f"Average days: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_rentals = [{"car": "sedan", "days": 3, "daily_rate": 45}, {"car": "van", "days": 2, "daily_rate": 70}]
rental_report(example_rentals, 10)
