def total_inventory(products):
    total = 0
    for item in products:
        total += item["stock"]
    return total

def average_inventory(products):
    if not products:
        return 0
    return total_inventory(products) / len(products)

def high_inventory(products, minimum):
    selected = []
    for item in products:
        if item["stock"] >= minimum:
            selected.append(item)
    return selected

def inventory_report(products, minimum):
    total = total_inventory(products)
    average = average_inventory(products)
    selected = high_inventory(products, minimum)
    print(f"Records         : {products}")
    print(f"Total stock  : {total}")
    print(f"Average stock: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_inventory = [{"sku": "A1", "stock": 8, "minimum": 5}, {"sku": "B2", "stock": 2, "minimum": 6}]
inventory_report(example_inventory, 10)
