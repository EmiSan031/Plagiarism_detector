def low_stock(products, limit):
    return [product["name"] for product in products if product["stock"] <= limit]

def inventory_value(products):
    return sum(product["stock"] * product["price"] for product in products)

def inventory_report(products):
    low = low_stock(products, 5)
    value = inventory_value(products)
    print("Low stock:", low)
    print("Inventory value: {:.2f}".format(value))
    return value

items = [{"name": "pen", "stock": 4, "price": 1.5}, {"name": "bag", "stock": 8, "price": 20}]
inventory_report(items)

def product_names(products):
    names = []
    for product in products:
        names.append(product.get("name", product.get("label", "")))
    return names

print(f"Products: {product_names(items) if 'items' in globals() else product_names(articles)}")

def describe_sample_size(values):
    size = 0
    for _ in values:
        size += 1
    if size == 0:
        return "empty"
    if size == 1:
        return "single"
    return "multiple"

print(describe_sample_size([1, 2, 3]))
