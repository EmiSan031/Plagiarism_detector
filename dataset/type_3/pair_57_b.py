def sum_weather_metric(records):
    amount = 0
    for row in records:
        if "temperature" in row:
            amount += row["temperature"]
    return amount

def mean_weather_metric(records):
    valid = [row for row in records if "temperature" in row]
    if not valid:
        return 0
    return sum_weather_metric(valid) / len(valid)

def choose_weather_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("temperature", 0)
        bonus = row.get("humidity", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_weather_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("temperature", 0) > best.get("temperature", 0):
            best = row
    return best

def describe_weather(records, floor_value):
    cleaned = [row for row in records if row.get("temperature", 0) >= 0]
    total = sum_weather_metric(cleaned)
    average = mean_weather_metric(cleaned)
    chosen = choose_weather_items(cleaned, floor_value)
    best = best_weather_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total temperature  : {total}")
    print(f"Average temperature: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_weather = [{"day": "Mon", "temperature": 24, "humidity": 61}, {"day": "Tue", "temperature": 27, "humidity": 55}]
describe_weather(sample_weather, 10)
