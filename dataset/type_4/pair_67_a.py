def total_invoices(lines):
    result = 0
    for item in lines:
        result = result + item["price"]
    return result

def average_invoices(lines):
    count = 0
    total = 0
    for item in lines:
        count += 1
        total += item["price"]
    if count == 0:
        return 0
    return total / count

def maximum_invoices(lines):
    if not lines:
        return None
    best = lines[0]
    for item in lines[1:]:
        if item["price"] > best["price"]:
            best = item
    return best

def select_invoices(lines, minimum):
    selected = []
    for item in lines:
        if item["price"] >= minimum:
            selected.append(item)
    return selected

def invoice_report(lines, minimum):
    total = total_invoices(lines)
    average = average_invoices(lines)
    best = maximum_invoices(lines)
    selected = select_invoices(lines, minimum)
    print(f"Total price: {total}")
    print(f"Average price: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_invoices = [{"item": "desk", "price": 180}, {"item": "lamp", "price": 40}, {"item": "chair", "price": 85}]
invoice_report(data_invoices, 10)
