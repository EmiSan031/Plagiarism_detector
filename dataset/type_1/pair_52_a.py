def total_ticketsales(shows):
    total = 0
    for item in shows:
        total += item["tickets"]
    return total

def average_ticketsales(shows):
    if not shows:
        return 0
    return total_ticketsales(shows) / len(shows)

def count_high_ticketsales(shows, minimum):
    count = 0
    for item in shows:
        if item["tickets"] >= minimum:
            count += 1
    return count

def ticket_sale_report(shows, minimum):
    total = total_ticketsales(shows)
    average = average_ticketsales(shows)
    high_count = count_high_ticketsales(shows, minimum)
    print(f"Total tickets: {total}")
    print(f"Average tickets: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_ticketsales = [{"show": "one", "tickets": 80}, {"show": "two", "tickets": 65}, {"show": "three", "tickets": 92}]
ticket_sale_report(records_ticketsales, 10)
