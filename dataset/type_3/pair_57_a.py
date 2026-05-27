def total_weather(readings):
    total = 0
    for item in readings:
        total += item["temperature"]
    return total

def average_weather(readings):
    if not readings:
        return 0
    return total_weather(readings) / len(readings)

def high_weather(readings, minimum):
    selected = []
    for item in readings:
        if item["temperature"] >= minimum:
            selected.append(item)
    return selected

def weather_report(readings, minimum):
    total = total_weather(readings)
    average = average_weather(readings)
    selected = high_weather(readings, minimum)
    print(f"Records         : {readings}")
    print(f"Total temperature  : {total}")
    print(f"Average temperature: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_weather = [{"day": "Mon", "temperature": 24, "humidity": 61}, {"day": "Tue", "temperature": 27, "humidity": 55}]
weather_report(example_weather, 10)
