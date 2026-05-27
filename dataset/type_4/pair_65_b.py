def total_recipes(ingredients):
    return sum(map(lambda entry: entry["quantity"], ingredients))

def average_recipes(ingredients):
    values = tuple(entry["quantity"] for entry in ingredients)
    return sum(values) / len(values) if values else 0

def maximum_recipes(ingredients):
    return max(ingredients, key=lambda entry: entry["quantity"], default=None)

def select_recipes(ingredients, minimum):
    return list(filter(lambda entry: entry["quantity"] >= minimum, ingredients))

def recipe_report(ingredients, minimum):
    summary = (
        total_recipes(ingredients),
        average_recipes(ingredients),
        maximum_recipes(ingredients),
        select_recipes(ingredients, minimum),
    )
    labels = ("Total quantity", "Average quantity", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_recipes = [{"item": "flour", "quantity": 500}, {"item": "milk", "quantity": 250}, {"item": "egg", "quantity": 3}]
recipe_report(data_recipes, 10)
