def total_exams(scores):
    total = 0
    for item in scores:
        total += item["score"]
    return total

def average_exams(scores):
    if not scores:
        return 0
    return total_exams(scores) / len(scores)

def high_exams(scores, minimum):
    selected = []
    for item in scores:
        if item["score"] >= minimum:
            selected.append(item)
    return selected

def exam_report(scores, minimum):
    total = total_exams(scores)
    average = average_exams(scores)
    selected = high_exams(scores, minimum)
    print(f"Records         : {scores}")
    print(f"Total score  : {total}")
    print(f"Average score: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_exams = [{"student": "Nora", "score": 82, "bonus": 3}, {"student": "Omar", "score": 71, "bonus": 5}]
exam_report(example_exams, 10)
