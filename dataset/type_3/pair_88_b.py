def sum_packets_metric(records):
    amount = 0
    for row in records:
        if "latency" in row:
            amount += row["latency"]
    return amount

def mean_packets_metric(records):
    valid = [row for row in records if "latency" in row]
    if not valid:
        return 0
    return sum_packets_metric(valid) / len(valid)

def choose_packets_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("latency", 0)
        bonus = row.get("loss", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_packets_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("latency", 0) > best.get("latency", 0):
            best = row
    return best

def describe_packets(records, floor_value):
    cleaned = [row for row in records if row.get("latency", 0) >= 0]
    total = sum_packets_metric(cleaned)
    average = mean_packets_metric(cleaned)
    chosen = choose_packets_items(cleaned, floor_value)
    best = best_packets_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total latency  : {total}")
    print(f"Average latency: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_packets = [{"host": "a", "latency": 34, "loss": 0}, {"host": "b", "latency": 71, "loss": 2}]
describe_packets(sample_packets, 10)
