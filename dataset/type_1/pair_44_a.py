def total_plantsales(sales):
    total = 0
    for item in sales:
        total += item["units"]
    return total

def average_plantsales(sales):
    if not sales:
        return 0
    return total_plantsales(sales) / len(sales)

def count_high_plantsales(sales, minimum):
    count = 0
    for item in sales:
        if item["units"] >= minimum:
            count += 1
    return count

def plant_sale_report(sales, minimum):
    total = total_plantsales(sales)
    average = average_plantsales(sales)
    high_count = count_high_plantsales(sales, minimum)
    print(f"Total units: {total}")
    print(f"Average units: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_plantsales = [{"item": "fern", "units": 9}, {"item": "cactus", "units": 14}, {"item": "ivy", "units": 6}]
plant_sale_report(records_plantsales, 10)
