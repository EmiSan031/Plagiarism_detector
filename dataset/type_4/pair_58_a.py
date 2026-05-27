def total_exams(scores):
    result = 0
    for item in scores:
        result = result + item["score"]
    return result

def average_exams(scores):
    count = 0
    total = 0
    for item in scores:
        count += 1
        total += item["score"]
    if count == 0:
        return 0
    return total / count

def maximum_exams(scores):
    if not scores:
        return None
    best = scores[0]
    for item in scores[1:]:
        if item["score"] > best["score"]:
            best = item
    return best

def select_exams(scores, minimum):
    selected = []
    for item in scores:
        if item["score"] >= minimum:
            selected.append(item)
    return selected

def exam_report(scores, minimum):
    total = total_exams(scores)
    average = average_exams(scores)
    best = maximum_exams(scores)
    selected = select_exams(scores, minimum)
    print(f"Total score: {total}")
    print(f"Average score: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_exams = [{"student": "Nora", "score": 82}, {"student": "Omar", "score": 71}, {"student": "Paz", "score": 94}]
exam_report(data_exams, 10)
