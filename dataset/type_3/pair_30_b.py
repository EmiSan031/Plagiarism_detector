def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def freezing_values(values):
    frozen = []
    for value in values:
        if value <= 0:
            frozen.append(value)
    return frozen

def temperature_report(values):
    converted = []
    for value in values:
        converted.append(celsius_to_fahrenheit(value))
    frozen = freezing_values(values)
    print(f"Celsius: {values}")
    print(f"Fahrenheit: {converted}")
    print(f"Freezing values: {frozen}")
    return converted

temperature_report([0, 20, 37])

def rounded_values(values):
    rounded = []
    for value in values:
        rounded.append(round(value, 2))
    return rounded

print(f"Rounded: {rounded_values(temperature_report([10, 15, 21]))}")
