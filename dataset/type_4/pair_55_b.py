def total_meals(meals):
    return sum(map(lambda entry: entry["calories"], meals))

def average_meals(meals):
    values = tuple(entry["calories"] for entry in meals)
    return sum(values) / len(values) if values else 0

def maximum_meals(meals):
    return max(meals, key=lambda entry: entry["calories"], default=None)

def select_meals(meals, minimum):
    return list(filter(lambda entry: entry["calories"] >= minimum, meals))

def meal_report(meals, minimum):
    summary = (
        total_meals(meals),
        average_meals(meals),
        maximum_meals(meals),
        select_meals(meals, minimum),
    )
    labels = ("Total calories", "Average calories", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_meals = [{"meal": "oats", "calories": 280}, {"meal": "salad", "calories": 190}, {"meal": "soup", "calories": 220}]
meal_report(data_meals, 10)
