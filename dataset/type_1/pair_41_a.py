def total_markets(stands):
    total = 0
    for item in stands:
        total += item["sales"]
    return total

def average_markets(stands):
    if not stands:
        return 0
    return total_markets(stands) / len(stands)

def count_high_markets(stands, minimum):
    count = 0
    for item in stands:
        if item["sales"] >= minimum:
            count += 1
    return count

def market_report(stands, minimum):
    total = total_markets(stands)
    average = average_markets(stands)
    high_count = count_high_markets(stands, minimum)
    print(f"Total sales: {total}")
    print(f"Average sales: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_markets = [{"stand": "fruit", "sales": 230}, {"stand": "bread", "sales": 180}, {"stand": "juice", "sales": 205}]
market_report(records_markets, 10)
