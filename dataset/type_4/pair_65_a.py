def total_recipes(ingredients):
    result = 0
    for item in ingredients:
        result = result + item["quantity"]
    return result

def average_recipes(ingredients):
    count = 0
    total = 0
    for item in ingredients:
        count += 1
        total += item["quantity"]
    if count == 0:
        return 0
    return total / count

def maximum_recipes(ingredients):
    if not ingredients:
        return None
    best = ingredients[0]
    for item in ingredients[1:]:
        if item["quantity"] > best["quantity"]:
            best = item
    return best

def select_recipes(ingredients, minimum):
    selected = []
    for item in ingredients:
        if item["quantity"] >= minimum:
            selected.append(item)
    return selected

def recipe_report(ingredients, minimum):
    total = total_recipes(ingredients)
    average = average_recipes(ingredients)
    best = maximum_recipes(ingredients)
    selected = select_recipes(ingredients, minimum)
    print(f"Total quantity: {total}")
    print(f"Average quantity: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_recipes = [{"item": "flour", "quantity": 500}, {"item": "milk", "quantity": 250}, {"item": "egg", "quantity": 3}]
recipe_report(data_recipes, 10)
