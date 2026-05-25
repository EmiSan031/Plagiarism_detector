def fahrenheit_to_celsius(values):
    converted = []
    for value in values:
        converted.append((value - 32) * 5 / 9)
    return converted

print(fahrenheit_to_celsius([32, 68, 104]))
