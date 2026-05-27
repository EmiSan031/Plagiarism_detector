def total_grades(grades):
    total = 0
    for item in grades:
        total += item["score"]
    return total

def average_grades(grades):
    if not grades:
        return 0
    return total_grades(grades) / len(grades)

def count_high_grades(grades, minimum):
    count = 0
    for item in grades:
        if item["score"] >= minimum:
            count += 1
    return count

def grade_report(grades, minimum):
    total = total_grades(grades)
    average = average_grades(grades)
    high_count = count_high_grades(grades, minimum)
    print(f"Total score: {total}")
    print(f"Average score: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_grades = [{"name": "Ana", "score": 91}, {"name": "Luis", "score": 78}, {"name": "Mia", "score": 86}]
grade_report(records_grades, 10)
