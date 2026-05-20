def parse_rows(lines):
    return [line.split(",") for line in lines]

def column_values(rows, index):
    return [row[index] for row in rows if index < len(row)]

def csv_report(lines):
    rows = parse_rows(lines)
    names = column_values(rows, 0)
    print("Rows:", len(rows))
    print("First column:", names)
    return rows

csv_report(["ana,10", "leo,12", "mia,9"])

def first_row(lines):
    rows = parse_rows(lines) if 'parse_rows' in globals() else split_records(lines)
    if rows:
        return rows[0]
    return []

print(f"First row: {first_row(['ana,10', 'leo,12'])}")

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
