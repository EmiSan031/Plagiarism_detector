def low_stock(products, limit):
    result = []
    for product in products:
        if product["stock"] <= limit:
            result.append(product["name"])
    return result

def inventory_value(products):
    total = 0
    for product in products:
        if product["stock"] > 0:
            total += product["stock"] * product["price"]
    return total

def most_expensive(products):
    selected = products[0]
    for product in products:
        if product["price"] > selected["price"]:
            selected = product
    return selected["name"]

def inventory_report(products):
    low = low_stock(products, 5)
    value = inventory_value(products)
    costly = most_expensive(products)
    print(f"Low stock: {low}")
    print(f"Inventory value: {value:.2f}")
    print(f"Most expensive: {costly}")
    return value

items = [{"name": "pen", "stock": 4, "price": 1.5}, {"name": "bag", "stock": 8, "price": 20}]
inventory_report(items)
