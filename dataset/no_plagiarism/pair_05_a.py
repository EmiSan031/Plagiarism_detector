def inventory_value(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total

print(inventory_value([{"price": 10, "quantity": 3}, {"price": 4, "quantity": 2}]))
