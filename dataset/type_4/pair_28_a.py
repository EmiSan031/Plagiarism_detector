def parse_rows(lines):
    rows = []
    for line in lines:
        parts = line.split(",")
        rows.append(parts)
    return rows

def column_values(rows, index):
    values = []
    for row in rows:
        if index < len(row):
            values.append(row[index])
    return values

def csv_report(lines):
    rows = parse_rows(lines)
    names = column_values(rows, 0)
    print(f"Rows: {len(rows)}")
    print(f"First column: {names}")
    return rows

csv_report(["ana,10", "leo,12", "mia,9"])

def first_row(lines):
    rows = parse_rows(lines) if 'parse_rows' in globals() else split_records(lines)
    if rows:
        return rows[0]
    return []

print(f"First row: {first_row(['ana,10', 'leo,12'])}")
