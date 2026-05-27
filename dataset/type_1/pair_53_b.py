# Type I clone: only comments and whitespace differ.

def total_cloud(servers):
    total = 0
    for item in servers:
        total += item["load"]
    return total


# Same function body as the original fragment.
def average_cloud(servers):
    if not servers:
        return 0
    return total_cloud(servers) / len(servers)


# Same function body as the original fragment.
def count_high_cloud(servers, minimum):
    count = 0
    for item in servers:
        if item["load"] >= minimum:
            count += 1
    return count


# Same function body as the original fragment.
def cloud_report(servers, minimum):
    total = total_cloud(servers)
    average = average_cloud(servers)
    high_count = count_high_cloud(servers, minimum)
    print(f"Total load: {total}")
    print(f"Average load: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_cloud = [{"host": "a", "load": 67}, {"host": "b", "load": 82}, {"host": "c", "load": 49}]
cloud_report(records_cloud, 10)
