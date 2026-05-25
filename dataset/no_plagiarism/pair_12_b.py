def top_students(records, minimum):
    result = []
    for name, grade in records:
        if grade >= minimum:
            result.append(name)
    return result

print(top_students([("Ana", 90), ("Luis", 65)], 80))
