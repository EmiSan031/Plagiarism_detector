def total_invoices(lines):
    return sum(map(lambda entry: entry["price"], lines))

def average_invoices(lines):
    values = tuple(entry["price"] for entry in lines)
    return sum(values) / len(values) if values else 0

def maximum_invoices(lines):
    return max(lines, key=lambda entry: entry["price"], default=None)

def select_invoices(lines, minimum):
    return list(filter(lambda entry: entry["price"] >= minimum, lines))

def invoice_report(lines, minimum):
    summary = (
        total_invoices(lines),
        average_invoices(lines),
        maximum_invoices(lines),
        select_invoices(lines, minimum),
    )
    labels = ("Total price", "Average price", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_invoices = [{"item": "desk", "price": 180}, {"item": "lamp", "price": 40}, {"item": "chair", "price": 85}]
invoice_report(data_invoices, 10)
