# Type I clone: only comments and whitespace differ.

def total_lessons(lessons):
    total = 0
    for item in lessons:
        total += item["minutes"]
    return total


# Same function body as the original fragment.
def average_lessons(lessons):
    if not lessons:
        return 0
    return total_lessons(lessons) / len(lessons)


# Same function body as the original fragment.
def count_high_lessons(lessons, minimum):
    count = 0
    for item in lessons:
        if item["minutes"] >= minimum:
            count += 1
    return count


# Same function body as the original fragment.
def lesson_report(lessons, minimum):
    total = total_lessons(lessons)
    average = average_lessons(lessons)
    high_count = count_high_lessons(lessons, minimum)
    print(f"Total minutes: {total}")
    print(f"Average minutes: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_lessons = [{"topic": "math", "minutes": 45}, {"topic": "art", "minutes": 35}, {"topic": "music", "minutes": 40}]
lesson_report(records_lessons, 10)
