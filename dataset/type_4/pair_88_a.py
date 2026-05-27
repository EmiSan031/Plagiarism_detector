def total_packets(packets):
    result = 0
    for item in packets:
        result = result + item["latency"]
    return result

def average_packets(packets):
    count = 0
    total = 0
    for item in packets:
        count += 1
        total += item["latency"]
    if count == 0:
        return 0
    return total / count

def maximum_packets(packets):
    if not packets:
        return None
    best = packets[0]
    for item in packets[1:]:
        if item["latency"] > best["latency"]:
            best = item
    return best

def select_packets(packets, minimum):
    selected = []
    for item in packets:
        if item["latency"] >= minimum:
            selected.append(item)
    return selected

def packet_report(packets, minimum):
    total = total_packets(packets)
    average = average_packets(packets)
    best = maximum_packets(packets)
    selected = select_packets(packets, minimum)
    print(f"Total latency: {total}")
    print(f"Average latency: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_packets = [{"host": "a", "latency": 34}, {"host": "b", "latency": 71}, {"host": "c", "latency": 28}]
packet_report(data_packets, 10)
