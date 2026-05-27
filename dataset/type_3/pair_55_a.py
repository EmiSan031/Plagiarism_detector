def total_meals(meals):
    total = 0
    for item in meals:
        total += item["calories"]
    return total

def average_meals(meals):
    if not meals:
        return 0
    return total_meals(meals) / len(meals)

def high_meals(meals, minimum):
    selected = []
    for item in meals:
        if item["calories"] >= minimum:
            selected.append(item)
    return selected

def meal_report(meals, minimum):
    total = total_meals(meals)
    average = average_meals(meals)
    selected = high_meals(meals, minimum)
    print(f"Records         : {meals}")
    print(f"Total calories  : {total}")
    print(f"Average calories: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_meals = [{"meal": "oats", "calories": 280, "protein": 11}, {"meal": "salad", "calories": 190, "protein": 7}]
meal_report(example_meals, 10)
