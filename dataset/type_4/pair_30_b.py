def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

def temperature_report(values):
    converted = list(map(celsius_to_fahrenheit, values))
    print("Celsius:", values)
    print("Fahrenheit:", converted)
    return converted

temperature_report([0, 20, 37])

def rounded_values(values):
    return [round(value, 2) for value in values]

print("Rounded:", rounded_values(temperature_report([10, 15, 21])))

def describe_sample_size(values):
    size = 0
    for _ in values:
        size += 1
    if size == 0:
        return "empty"
    if size == 1:
        return "single"
    return "multiple"

print(describe_sample_size([1, 2, 3]))
