def total_rentals(cars):
    return sum(map(lambda entry: entry["days"], cars))

def average_rentals(cars):
    values = tuple(entry["days"] for entry in cars)
    return sum(values) / len(values) if values else 0

def maximum_rentals(cars):
    return max(cars, key=lambda entry: entry["days"], default=None)

def select_rentals(cars, minimum):
    return list(filter(lambda entry: entry["days"] >= minimum, cars))

def rental_report(cars, minimum):
    summary = (
        total_rentals(cars),
        average_rentals(cars),
        maximum_rentals(cars),
        select_rentals(cars, minimum),
    )
    labels = ("Total days", "Average days", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_rentals = [{"car": "sedan", "days": 3}, {"car": "van", "days": 2}, {"car": "truck", "days": 6}]
rental_report(data_rentals, 10)
