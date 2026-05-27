def total_weather(readings):
    return sum(map(lambda entry: entry["temperature"], readings))

def average_weather(readings):
    values = tuple(entry["temperature"] for entry in readings)
    return sum(values) / len(values) if values else 0

def maximum_weather(readings):
    return max(readings, key=lambda entry: entry["temperature"], default=None)

def select_weather(readings, minimum):
    return list(filter(lambda entry: entry["temperature"] >= minimum, readings))

def weather_report(readings, minimum):
    summary = (
        total_weather(readings),
        average_weather(readings),
        maximum_weather(readings),
        select_weather(readings, minimum),
    )
    labels = ("Total temperature", "Average temperature", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_weather = [{"day": "Mon", "temperature": 24}, {"day": "Tue", "temperature": 27}, {"day": "Wed", "temperature": 21}]
weather_report(data_weather, 10)
