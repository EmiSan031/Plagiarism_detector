# Type I clone: only comments and whitespace differ.

def total_orders(orders):
    total = 0
    for item in orders:
        total += item["total"]
    return total


# Same function body as the original fragment.
def average_orders(orders):
    if not orders:
        return 0
    return total_orders(orders) / len(orders)


# Same function body as the original fragment.
def count_high_orders(orders, minimum):
    count = 0
    for item in orders:
        if item["total"] >= minimum:
            count += 1
    return count


# Same function body as the original fragment.
def order_report(orders, minimum):
    total = total_orders(orders)
    average = average_orders(orders)
    high_count = count_high_orders(orders, minimum)
    print(f"Total total: {total}")
    print(f"Average total: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_orders = [{"id": 1, "total": 120}, {"id": 2, "total": 85}, {"id": 3, "total": 150}]
order_report(records_orders, 10)
