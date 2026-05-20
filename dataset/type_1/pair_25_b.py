def low_stock(products, limit):
    result = []
    for product in products:
        if product["stock"] <= limit:
            result.append(product["name"])
    return result

def inventory_value(products):
    total = 0
    for product in products:
        total += product["stock"] * product["price"]
    return total

# Display low-stock items and total inventory value.
def inventory_report(products):
    low = low_stock(products, 5)
    value = inventory_value(products)
    print(f"Low stock: {low}")
    print(f"Inventory value: {value:.2f}")
    return value

items = [{"name": "pen", "stock": 4, "price": 1.5}, {"name": "bag", "stock": 8, "price": 20}]
inventory_report(items)

def product_names(products):
    names = []
    for product in products:
        names.append(product.get("name", product.get("label", "")))
    return names

print(f"Products: {product_names(items) if 'items' in globals() else product_names(articles)}")
