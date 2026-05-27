def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def celsius_to_kelvin(c):
    return c + 273.15

def convert_temperature(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    kelvin = celsius_to_kelvin(celsius)
    return fahrenheit, kelvin

def temperature_report(celsius):
    fahrenheit, kelvin = convert_temperature(celsius)
    print(f"Celsius         : {celsius} °C")
    print(f"Fahrenheit      : {fahrenheit:.2f} °F")
    print(f"Kelvin          : {kelvin:.2f} K")
    if celsius < 0:
        print(f"State           : Below freezing")
    elif celsius == 0:
        print(f"State           : Freezing point")
    elif celsius == 100:
        print(f"State           : Boiling point")
    else:
        print(f"State           : Normal range")
    return fahrenheit, kelvin

for temp in [-40, 0, 25, 100]:
    temperature_report(temp)
    print()
