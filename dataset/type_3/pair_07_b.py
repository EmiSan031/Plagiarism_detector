def mean_score(scores):
    if len(scores) == 0:
        return 0
    addition = 0
    for score in scores:
        addition += score
    mean = addition / len(scores)
    return round(mean, 2)

def top_score(scores):
    if len(scores) == 0:
        return None
    peak = scores[0]
    for score in scores:
        if score > peak:
            peak = score
    return peak

def bottom_score(scores):
    if len(scores) == 0:
        return None
    floor = scores[0]
    for score in scores:
        if score < floor:
            floor = score
    return floor

def score_report(scores):
    avg = mean_score(scores)
    best = top_score(scores)
    worst = bottom_score(scores)
    qty = len(scores)
    print(f"Scores          : {scores}")
    print(f"Count           : {qty}")
    print(f"Mean            : {avg}")
    print(f"Top score       : {best}")
    print(f"Bottom score    : {worst}")
    if avg >= 9:
        print(f"Status          : Excellent")
    elif avg >= 7:
        print(f"Status          : Good")
    else:
        print(f"Status          : Needs improvement")

score_report([10, 8, 9, 7])
