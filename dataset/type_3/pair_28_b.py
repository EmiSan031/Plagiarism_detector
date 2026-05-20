def parse_rows(lines):
    rows = []
    for line in lines:
        if line.strip():
            parts = line.split(",")
            rows.append(parts)
    return rows

def column_values(rows, index):
    values = []
    for row in rows:
        if index < len(row):
            values.append(row[index].strip())
    return values

def row_lengths(rows):
    lengths = []
    for row in rows:
        lengths.append(len(row))
    return lengths

def csv_report(lines):
    rows = parse_rows(lines)
    names = column_values(rows, 0)
    lengths = row_lengths(rows)
    print(f"Rows: {len(rows)}")
    print(f"First column: {names}")
    print(f"Columns per row: {lengths}")
    return rows

csv_report(["ana,10", "leo,12", "", "mia,9"])
