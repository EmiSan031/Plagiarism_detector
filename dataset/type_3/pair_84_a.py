def total_irrigation(plots):
    total = 0
    for item in plots:
        total += item["liters"]
    return total

def average_irrigation(plots):
    if not plots:
        return 0
    return total_irrigation(plots) / len(plots)

def high_irrigation(plots, minimum):
    selected = []
    for item in plots:
        if item["liters"] >= minimum:
            selected.append(item)
    return selected

def irrigation_report(plots, minimum):
    total = total_irrigation(plots)
    average = average_irrigation(plots)
    selected = high_irrigation(plots, minimum)
    print(f"Records         : {plots}")
    print(f"Total liters  : {total}")
    print(f"Average liters: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_irrigation = [{"plot": "east", "liters": 300, "area": 40}, {"plot": "west", "liters": 260, "area": 35}]
irrigation_report(example_irrigation, 10)
