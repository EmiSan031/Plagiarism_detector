def total_meals(meals):
    result = 0
    for item in meals:
        result = result + item["calories"]
    return result

def average_meals(meals):
    count = 0
    total = 0
    for item in meals:
        count += 1
        total += item["calories"]
    if count == 0:
        return 0
    return total / count

def maximum_meals(meals):
    if not meals:
        return None
    best = meals[0]
    for item in meals[1:]:
        if item["calories"] > best["calories"]:
            best = item
    return best

def select_meals(meals, minimum):
    selected = []
    for item in meals:
        if item["calories"] >= minimum:
            selected.append(item)
    return selected

def meal_report(meals, minimum):
    total = total_meals(meals)
    average = average_meals(meals)
    best = maximum_meals(meals)
    selected = select_meals(meals, minimum)
    print(f"Total calories: {total}")
    print(f"Average calories: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_meals = [{"meal": "oats", "calories": 280}, {"meal": "salad", "calories": 190}, {"meal": "soup", "calories": 220}]
meal_report(data_meals, 10)
