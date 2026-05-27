def total_quiz(answers):
    result = 0
    for item in answers:
        result = result + item["points"]
    return result

def average_quiz(answers):
    count = 0
    total = 0
    for item in answers:
        count += 1
        total += item["points"]
    if count == 0:
        return 0
    return total / count

def maximum_quiz(answers):
    if not answers:
        return None
    best = answers[0]
    for item in answers[1:]:
        if item["points"] > best["points"]:
            best = item
    return best

def select_quiz(answers, minimum):
    selected = []
    for item in answers:
        if item["points"] >= minimum:
            selected.append(item)
    return selected

def quiz_report(answers, minimum):
    total = total_quiz(answers)
    average = average_quiz(answers)
    best = maximum_quiz(answers)
    selected = select_quiz(answers, minimum)
    print(f"Total points: {total}")
    print(f"Average points: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_quiz = [{"q": 1, "points": 2}, {"q": 2, "points": 3}, {"q": 3, "points": 5}]
quiz_report(data_quiz, 10)
