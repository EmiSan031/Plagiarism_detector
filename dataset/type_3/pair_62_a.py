def total_routes(segments):
    total = 0
    for item in segments:
        total += item["distance"]
    return total

def average_routes(segments):
    if not segments:
        return 0
    return total_routes(segments) / len(segments)

def high_routes(segments, minimum):
    selected = []
    for item in segments:
        if item["distance"] >= minimum:
            selected.append(item)
    return selected

def route_report(segments, minimum):
    total = total_routes(segments)
    average = average_routes(segments)
    selected = high_routes(segments, minimum)
    print(f"Records         : {segments}")
    print(f"Total distance  : {total}")
    print(f"Average distance: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_routes = [{"name": "north", "distance": 12, "time": 28}, {"name": "west", "distance": 7, "time": 20}]
route_report(example_routes, 10)
