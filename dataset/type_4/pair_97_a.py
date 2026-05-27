def total_rentals(cars):
    result = 0
    for item in cars:
        result = result + item["days"]
    return result

def average_rentals(cars):
    count = 0
    total = 0
    for item in cars:
        count += 1
        total += item["days"]
    if count == 0:
        return 0
    return total / count

def maximum_rentals(cars):
    if not cars:
        return None
    best = cars[0]
    for item in cars[1:]:
        if item["days"] > best["days"]:
            best = item
    return best

def select_rentals(cars, minimum):
    selected = []
    for item in cars:
        if item["days"] >= minimum:
            selected.append(item)
    return selected

def rental_report(cars, minimum):
    total = total_rentals(cars)
    average = average_rentals(cars)
    best = maximum_rentals(cars)
    selected = select_rentals(cars, minimum)
    print(f"Total days: {total}")
    print(f"Average days: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_rentals = [{"car": "sedan", "days": 3}, {"car": "van", "days": 2}, {"car": "truck", "days": 6}]
rental_report(data_rentals, 10)
