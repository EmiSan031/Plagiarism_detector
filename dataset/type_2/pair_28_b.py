def split_records(records):
    table = []
    for record in records:
        fields = record.split(",")
        table.append(fields)
    return table

def field_values(table, position):
    items = []
    for fields in table:
        if position < len(fields):
            items.append(fields[position])
    return items

def record_report(records):
    table = split_records(records)
    first_fields = field_values(table, 0)
    print(f"Record count: {len(table)}")
    print(f"First fields: {first_fields}")
    return table

record_report(["red,5", "blue,8", "green,3"])

def first_row(lines):
    rows = parse_rows(lines) if 'parse_rows' in globals() else split_records(lines)
    if rows:
        return rows[0]
    return []

print(f"First row: {first_row(['ana,10', 'leo,12'])}")
