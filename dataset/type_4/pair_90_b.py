def total_quiz(answers):
    return sum(map(lambda entry: entry["points"], answers))

def average_quiz(answers):
    values = tuple(entry["points"] for entry in answers)
    return sum(values) / len(values) if values else 0

def maximum_quiz(answers):
    return max(answers, key=lambda entry: entry["points"], default=None)

def select_quiz(answers, minimum):
    return list(filter(lambda entry: entry["points"] >= minimum, answers))

def quiz_report(answers, minimum):
    summary = (
        total_quiz(answers),
        average_quiz(answers),
        maximum_quiz(answers),
        select_quiz(answers, minimum),
    )
    labels = ("Total points", "Average points", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_quiz = [{"q": 1, "points": 2}, {"q": 2, "points": 3}, {"q": 3, "points": 5}]
quiz_report(data_quiz, 10)
