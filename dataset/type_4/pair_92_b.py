def total_courses(courses):
    return sum(map(lambda entry: entry["credits"], courses))

def average_courses(courses):
    values = tuple(entry["credits"] for entry in courses)
    return sum(values) / len(values) if values else 0

def maximum_courses(courses):
    return max(courses, key=lambda entry: entry["credits"], default=None)

def select_courses(courses, minimum):
    return list(filter(lambda entry: entry["credits"] >= minimum, courses))

def course_report(courses, minimum):
    summary = (
        total_courses(courses),
        average_courses(courses),
        maximum_courses(courses),
        select_courses(courses, minimum),
    )
    labels = ("Total credits", "Average credits", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_courses = [{"code": "CS1", "credits": 6}, {"code": "MA1", "credits": 5}, {"code": "HI1", "credits": 4}]
course_report(data_courses, 10)
