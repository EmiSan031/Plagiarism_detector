def total_weather(readings):
    result = 0
    for item in readings:
        result = result + item["temperature"]
    return result

def average_weather(readings):
    count = 0
    total = 0
    for item in readings:
        count += 1
        total += item["temperature"]
    if count == 0:
        return 0
    return total / count

def maximum_weather(readings):
    if not readings:
        return None
    best = readings[0]
    for item in readings[1:]:
        if item["temperature"] > best["temperature"]:
            best = item
    return best

def select_weather(readings, minimum):
    selected = []
    for item in readings:
        if item["temperature"] >= minimum:
            selected.append(item)
    return selected

def weather_report(readings, minimum):
    total = total_weather(readings)
    average = average_weather(readings)
    best = maximum_weather(readings)
    selected = select_weather(readings, minimum)
    print(f"Total temperature: {total}")
    print(f"Average temperature: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_weather = [{"day": "Mon", "temperature": 24}, {"day": "Tue", "temperature": 27}, {"day": "Wed", "temperature": 21}]
weather_report(data_weather, 10)
