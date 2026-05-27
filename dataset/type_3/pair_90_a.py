def total_quiz(answers):
    total = 0
    for item in answers:
        total += item["correct"]
    return total

def average_quiz(answers):
    if not answers:
        return 0
    return total_quiz(answers) / len(answers)

def high_quiz(answers, minimum):
    selected = []
    for item in answers:
        if item["correct"] >= minimum:
            selected.append(item)
    return selected

def quiz_report(answers, minimum):
    total = total_quiz(answers)
    average = average_quiz(answers)
    selected = high_quiz(answers, minimum)
    print(f"Records         : {answers}")
    print(f"Total correct  : {total}")
    print(f"Average correct: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_quiz = [{"q": 1, "correct": True, "points": 2}, {"q": 2, "correct": False, "points": 3}]
quiz_report(example_quiz, 10)
