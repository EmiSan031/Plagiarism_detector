def total_exams(scores):
    return sum(map(lambda entry: entry["score"], scores))

def average_exams(scores):
    values = tuple(entry["score"] for entry in scores)
    return sum(values) / len(values) if values else 0

def maximum_exams(scores):
    return max(scores, key=lambda entry: entry["score"], default=None)

def select_exams(scores, minimum):
    return list(filter(lambda entry: entry["score"] >= minimum, scores))

def exam_report(scores, minimum):
    summary = (
        total_exams(scores),
        average_exams(scores),
        maximum_exams(scores),
        select_exams(scores, minimum),
    )
    labels = ("Total score", "Average score", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_exams = [{"student": "Nora", "score": 82}, {"student": "Omar", "score": 71}, {"student": "Paz", "score": 94}]
exam_report(data_exams, 10)
