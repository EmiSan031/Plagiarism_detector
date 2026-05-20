# Convert Celsius values into Fahrenheit values.
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def temperature_report(values):
    converted = []
    for value in values:
        converted.append(celsius_to_fahrenheit(value))
    print(f"Celsius: {values}")
    print(f"Fahrenheit: {converted}")
    return converted

temperature_report([0, 20, 37])

def rounded_values(values):
    rounded = []
    for value in values:
        rounded.append(round(value, 2))
    return rounded

print(f"Rounded: {rounded_values(temperature_report([10, 15, 21]))}")

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
