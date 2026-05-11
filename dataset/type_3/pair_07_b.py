def mean_score(scores):
    if len(scores) == 0:
        return 0
    addition = 0
    for score in scores:
        addition += score
    mean = addition / len(scores)
    return round(mean, 2)


print(mean_score([10, 8, 9, 7]))
