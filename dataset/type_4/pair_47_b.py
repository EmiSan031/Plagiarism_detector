import bisect

def letter_grade(score):
    thresholds = [60, 70, 80, 90]
    grades = ["F", "D", "C", "B", "A"]
    return grades[bisect.bisect_left(thresholds, score)]

def grade_all(scores):
    return list(map(letter_grade, scores))

def class_average(scores):
    return sum(scores) / len(scores)

def passing_count(scores):
    return sum(1 for s in scores if s >= 60)

scores = [95, 82, 74, 61, 58, 90, 67, 45]
print([letter_grade(s) for s in scores])
print(grade_all(scores))
print(class_average(scores))
print(passing_count(scores))
