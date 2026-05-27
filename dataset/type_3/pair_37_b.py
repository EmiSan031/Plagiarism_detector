def to_fahrenheit(degrees):
    return degrees * 9 / 5 + 32

def to_kelvin(degrees):
    if degrees < -273.15:
        return None
    return degrees + 273.15

def human_comfort(degrees):
    if degrees < 10:
        return "Cold"
    elif degrees <= 25:
        return "Comfortable"
    elif degrees <= 35:
        return "Warm"
    else:
        return "Hot"

def conversion_report(degrees):
    fahr = to_fahrenheit(degrees)
    kelv = to_kelvin(degrees)
    comfort = human_comfort(degrees)
    print(f"Input (Celsius) : {degrees} °C")
    print(f"Fahrenheit      : {fahr:.2f} °F")
    if kelv is not None:
        print(f"Kelvin          : {kelv:.2f} K")
    else:
        print(f"Kelvin          : Below absolute zero — invalid")
    print(f"Comfort level   : {comfort}")
    if degrees < 0:
        print(f"Phase note      : Below freezing")
    elif degrees == 0:
        print(f"Phase note      : Freezing point")
    elif degrees == 100:
        print(f"Phase note      : Boiling point")
    else:
        print(f"Phase note      : Normal range")
    return fahr, kelv

for deg in [-40, 0, 25, 100]:
    conversion_report(deg)
    print()
