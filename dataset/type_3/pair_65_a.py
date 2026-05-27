def total_recipes(ingredients):
    total = 0
    for item in ingredients:
        total += item["quantity"]
    return total

def average_recipes(ingredients):
    if not ingredients:
        return 0
    return total_recipes(ingredients) / len(ingredients)

def high_recipes(ingredients, minimum):
    selected = []
    for item in ingredients:
        if item["quantity"] >= minimum:
            selected.append(item)
    return selected

def recipe_report(ingredients, minimum):
    total = total_recipes(ingredients)
    average = average_recipes(ingredients)
    selected = high_recipes(ingredients, minimum)
    print(f"Records         : {ingredients}")
    print(f"Total quantity  : {total}")
    print(f"Average quantity: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_recipes = [{"item": "flour", "quantity": 500, "factor": 2}, {"item": "milk", "quantity": 250, "factor": 2}]
recipe_report(example_recipes, 10)
