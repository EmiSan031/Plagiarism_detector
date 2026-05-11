def mean_score(scores):
    addition = 0
    for score in scores:
        addition += score
    return addition / len(scores)


print(mean_score([95, 87, 91, 89]))
