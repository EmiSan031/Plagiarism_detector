def passing_scores(scores, minimum):
    return list(filter(lambda score: score >= minimum, scores))

def average_score(scores):
    return sum(scores) / len(scores)

def class_summary(scores):
    passing = passing_scores(scores, 70)
    average = average_score(scores)
    print("Average: {:.2f}".format(average))
    print("Passing:", len(passing))
    return average

class_summary([88, 61, 74, 95, 69])

def failing_scores(scores, minimum):
    result = []
    for score in scores:
        if score < minimum:
            result.append(score)
    return result

print(f"Failing: {failing_scores([88, 61, 74, 95, 69], 70)}")

def describe_sample_size(values):
    size = 0
    for _ in values:
        size += 1
    if size == 0:
        return "empty"
    if size == 1:
        return "single"
    return "multiple"

print(describe_sample_size([1, 2, 3]))
