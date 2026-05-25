def normalize_scores(scores):
    highest = max(scores)
    if highest == 0:
        return scores
    return [score / highest for score in scores]

print(normalize_scores([10, 20, 40]))
