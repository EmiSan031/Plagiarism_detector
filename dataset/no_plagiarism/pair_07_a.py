def parse_csv_line(line):
    values = []
    current = ""
    for char in line:
        if char == ",":
            values.append(current.strip())
            current = ""
        else:
            current += char
    values.append(current.strip())
    return values

print(parse_csv_line("name, age, city"))
