def total_courses(courses):
    result = 0
    for item in courses:
        result = result + item["credits"]
    return result

def average_courses(courses):
    count = 0
    total = 0
    for item in courses:
        count += 1
        total += item["credits"]
    if count == 0:
        return 0
    return total / count

def maximum_courses(courses):
    if not courses:
        return None
    best = courses[0]
    for item in courses[1:]:
        if item["credits"] > best["credits"]:
            best = item
    return best

def select_courses(courses, minimum):
    selected = []
    for item in courses:
        if item["credits"] >= minimum:
            selected.append(item)
    return selected

def course_report(courses, minimum):
    total = total_courses(courses)
    average = average_courses(courses)
    best = maximum_courses(courses)
    selected = select_courses(courses, minimum)
    print(f"Total credits: {total}")
    print(f"Average credits: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_courses = [{"code": "CS1", "credits": 6}, {"code": "MA1", "credits": 5}, {"code": "HI1", "credits": 4}]
course_report(data_courses, 10)
