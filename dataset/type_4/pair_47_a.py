def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def grade_all(scores):
    result = []
    for score in scores:
        result.append(letter_grade(score))
    return result

def class_average(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

def passing_count(scores):
    count = 0
    for score in scores:
        if score >= 60:
            count += 1
    return count

scores = [95, 82, 74, 61, 58, 90, 67, 45]
print([letter_grade(s) for s in scores])
print(grade_all(scores))
print(class_average(scores))
print(passing_count(scores))
