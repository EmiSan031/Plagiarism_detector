def approved_marks(marks, floor):
    selected = []
    for mark in marks:
        if mark >= floor:
            selected.append(mark)
    return selected

def mean_mark(marks):
    amount = 0
    for mark in marks:
        amount += mark
    return amount / len(marks)

def group_summary(marks):
    approved = approved_marks(marks, 65)
    mean = mean_mark(marks)
    print(f"Mean mark: {mean:.2f}")
    print(f"Approved: {len(approved)}")
    return mean

group_summary([92, 55, 68, 81, 73])

def failing_scores(scores, minimum):
    result = []
    for score in scores:
        if score < minimum:
            result.append(score)
    return result

print(f"Failing: {failing_scores([88, 61, 74, 95, 69], 70)}")
