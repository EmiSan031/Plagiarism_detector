def total_irrigation(plots):
    result = 0
    for item in plots:
        result = result + item["liters"]
    return result

def average_irrigation(plots):
    count = 0
    total = 0
    for item in plots:
        count += 1
        total += item["liters"]
    if count == 0:
        return 0
    return total / count

def maximum_irrigation(plots):
    if not plots:
        return None
    best = plots[0]
    for item in plots[1:]:
        if item["liters"] > best["liters"]:
            best = item
    return best

def select_irrigation(plots, minimum):
    selected = []
    for item in plots:
        if item["liters"] >= minimum:
            selected.append(item)
    return selected

def irrigation_report(plots, minimum):
    total = total_irrigation(plots)
    average = average_irrigation(plots)
    best = maximum_irrigation(plots)
    selected = select_irrigation(plots, minimum)
    print(f"Total liters: {total}")
    print(f"Average liters: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_irrigation = [{"plot": "east", "liters": 300}, {"plot": "west", "liters": 260}, {"plot": "north", "liters": 410}]
irrigation_report(data_irrigation, 10)
