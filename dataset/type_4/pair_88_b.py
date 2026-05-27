def total_packets(packets):
    return sum(map(lambda entry: entry["latency"], packets))

def average_packets(packets):
    values = tuple(entry["latency"] for entry in packets)
    return sum(values) / len(values) if values else 0

def maximum_packets(packets):
    return max(packets, key=lambda entry: entry["latency"], default=None)

def select_packets(packets, minimum):
    return list(filter(lambda entry: entry["latency"] >= minimum, packets))

def packet_report(packets, minimum):
    summary = (
        total_packets(packets),
        average_packets(packets),
        maximum_packets(packets),
        select_packets(packets, minimum),
    )
    labels = ("Total latency", "Average latency", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_packets = [{"host": "a", "latency": 34}, {"host": "b", "latency": 71}, {"host": "c", "latency": 28}]
packet_report(data_packets, 10)
