def total_routes(segments):
    result = 0
    for item in segments:
        result = result + item["distance"]
    return result

def average_routes(segments):
    count = 0
    total = 0
    for item in segments:
        count += 1
        total += item["distance"]
    if count == 0:
        return 0
    return total / count

def maximum_routes(segments):
    if not segments:
        return None
    best = segments[0]
    for item in segments[1:]:
        if item["distance"] > best["distance"]:
            best = item
    return best

def select_routes(segments, minimum):
    selected = []
    for item in segments:
        if item["distance"] >= minimum:
            selected.append(item)
    return selected

def route_report(segments, minimum):
    total = total_routes(segments)
    average = average_routes(segments)
    best = maximum_routes(segments)
    selected = select_routes(segments, minimum)
    print(f"Total distance: {total}")
    print(f"Average distance: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_routes = [{"name": "north", "distance": 12}, {"name": "west", "distance": 7}, {"name": "south", "distance": 18}]
route_report(data_routes, 10)
