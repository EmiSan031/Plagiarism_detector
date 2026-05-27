def total_bakerysales(batches):
    total = 0
    for item in batches:
        total += item["sold"]
    return total

def average_bakerysales(batches):
    if not batches:
        return 0
    return total_bakerysales(batches) / len(batches)

def count_high_bakerysales(batches, minimum):
    count = 0
    for item in batches:
        if item["sold"] >= minimum:
            count += 1
    return count

def bakery_sale_report(batches, minimum):
    total = total_bakerysales(batches)
    average = average_bakerysales(batches)
    high_count = count_high_bakerysales(batches, minimum)
    print(f"Total sold: {total}")
    print(f"Average sold: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_bakerysales = [{"batch": "am", "sold": 54}, {"batch": "pm", "sold": 61}, {"batch": "eve", "sold": 42}]
bakery_sale_report(records_bakerysales, 10)
