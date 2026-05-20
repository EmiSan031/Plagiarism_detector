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
    if not scores:
        return 0
    return total / len(scores)

def highest_score(scores):
    highest = scores[0]
    for score in scores:
        if score > highest:
            highest = score
    return highest

def class_summary(scores):
    passing = passing_scores(scores, 70)
    average = average_score(scores)
    highest = highest_score(scores)
    print(f"Average: {average:.2f}")
    print(f"Passing: {len(passing)}")
    print(f"Highest: {highest}")
    return average

class_summary([88, 61, 74, 95, 69])
