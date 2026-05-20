def passing_scores(scores, minimum):
    result = []
    for score in scores:
        if score >= minimum:
            result.append(score)
    return result

def average_score(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

def class_summary(scores):
    passing = passing_scores(scores, 70)
    average = average_score(scores)
    print(f"Average: {average:.2f}")
    print(f"Passing: {len(passing)}")
    return average

class_summary([88, 61, 74, 95, 69])

def failing_scores(scores, minimum):
    result = []
    for score in scores:
        if score < minimum:
            result.append(score)
    return result

print(f"Failing: {failing_scores([88, 61, 74, 95, 69], 70)}")
