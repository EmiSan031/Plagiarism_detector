# Type I clone: only comments and whitespace differ.

def total_rent(homes):
    total = 0
    for item in homes:
        total += item["price"]
    return total


# Same function body as the original fragment.
def average_rent(homes):
    if not homes:
        return 0
    return total_rent(homes) / len(homes)


# Same function body as the original fragment.
def count_high_rent(homes, minimum):
    count = 0
    for item in homes:
        if item["price"] >= minimum:
            count += 1
    return count


# Same function body as the original fragment.
def rent_report(homes, minimum):
    total = total_rent(homes)
    average = average_rent(homes)
    high_count = count_high_rent(homes, minimum)
    print(f"Total price: {total}")
    print(f"Average price: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_rent = [{"unit": "A", "price": 700}, {"unit": "B", "price": 820}, {"unit": "C", "price": 650}]
rent_report(records_rent, 10)
