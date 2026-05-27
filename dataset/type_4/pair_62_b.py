def total_routes(segments):
    return sum(map(lambda entry: entry["distance"], segments))

def average_routes(segments):
    values = tuple(entry["distance"] for entry in segments)
    return sum(values) / len(values) if values else 0

def maximum_routes(segments):
    return max(segments, key=lambda entry: entry["distance"], default=None)

def select_routes(segments, minimum):
    return list(filter(lambda entry: entry["distance"] >= minimum, segments))

def route_report(segments, minimum):
    summary = (
        total_routes(segments),
        average_routes(segments),
        maximum_routes(segments),
        select_routes(segments, minimum),
    )
    labels = ("Total distance", "Average distance", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_routes = [{"name": "north", "distance": 12}, {"name": "west", "distance": 7}, {"name": "south", "distance": 18}]
route_report(data_routes, 10)
