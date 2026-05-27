def total_courses(courses):
    total = 0
    for item in courses:
        total += item["credits"]
    return total

def average_courses(courses):
    if not courses:
        return 0
    return total_courses(courses) / len(courses)

def high_courses(courses, minimum):
    selected = []
    for item in courses:
        if item["credits"] >= minimum:
            selected.append(item)
    return selected

def course_report(courses, minimum):
    total = total_courses(courses)
    average = average_courses(courses)
    selected = high_courses(courses, minimum)
    print(f"Records         : {courses}")
    print(f"Total credits  : {total}")
    print(f"Average credits: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_courses = [{"code": "CS1", "credits": 6, "passed": True}, {"code": "MA1", "credits": 5, "passed": False}]
course_report(example_courses, 10)
