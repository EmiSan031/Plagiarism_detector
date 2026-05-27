def total_inventory(products):
    result = 0
    for item in products:
        result = result + item["stock"]
    return result

def average_inventory(products):
    count = 0
    total = 0
    for item in products:
        count += 1
        total += item["stock"]
    if count == 0:
        return 0
    return total / count

def maximum_inventory(products):
    if not products:
        return None
    best = products[0]
    for item in products[1:]:
        if item["stock"] > best["stock"]:
            best = item
    return best

def select_inventory(products, minimum):
    selected = []
    for item in products:
        if item["stock"] >= minimum:
            selected.append(item)
    return selected

def inventory_report(products, minimum):
    total = total_inventory(products)
    average = average_inventory(products)
    best = maximum_inventory(products)
    selected = select_inventory(products, minimum)
    print(f"Total stock: {total}")
    print(f"Average stock: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_inventory = [{"sku": "A1", "stock": 8}, {"sku": "B2", "stock": 2}, {"sku": "C3", "stock": 11}]
inventory_report(data_inventory, 10)
