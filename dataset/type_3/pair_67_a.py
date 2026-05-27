def total_invoices(lines):
    total = 0
    for item in lines:
        total += item["price"]
    return total

def average_invoices(lines):
    if not lines:
        return 0
    return total_invoices(lines) / len(lines)

def high_invoices(lines, minimum):
    selected = []
    for item in lines:
        if item["price"] >= minimum:
            selected.append(item)
    return selected

def invoice_report(lines, minimum):
    total = total_invoices(lines)
    average = average_invoices(lines)
    selected = high_invoices(lines, minimum)
    print(f"Records         : {lines}")
    print(f"Total price  : {total}")
    print(f"Average price: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_invoices = [{"item": "desk", "price": 180, "tax": 0.16}, {"item": "lamp", "price": 40, "tax": 0.16}]
invoice_report(example_invoices, 10)
