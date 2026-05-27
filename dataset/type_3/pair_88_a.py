def total_packets(packets):
    total = 0
    for item in packets:
        total += item["latency"]
    return total

def average_packets(packets):
    if not packets:
        return 0
    return total_packets(packets) / len(packets)

def high_packets(packets, minimum):
    selected = []
    for item in packets:
        if item["latency"] >= minimum:
            selected.append(item)
    return selected

def packet_report(packets, minimum):
    total = total_packets(packets)
    average = average_packets(packets)
    selected = high_packets(packets, minimum)
    print(f"Records         : {packets}")
    print(f"Total latency  : {total}")
    print(f"Average latency: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_packets = [{"host": "a", "latency": 34, "loss": 0}, {"host": "b", "latency": 71, "loss": 2}]
packet_report(example_packets, 10)
