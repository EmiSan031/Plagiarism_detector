def mean_score(scores):
    addition = 0
    for score in scores:
        addition += score
    return addition / len(scores)

def top_score(scores):
    peak = scores[0]
    for score in scores:
        if score > peak:
            peak = score
    return peak

def bottom_score(scores):
    floor = scores[0]
    for score in scores:
        if score < floor:
            floor = score
    return floor

def student_report(scores):
    avg = mean_score(scores)
    best = top_score(scores)
    worst = bottom_score(scores)
    qty = len(scores)
    print(f"Score list      : {scores}")
    print(f"Number of scores: {qty}")
    print(f"Mean score      : {avg:.2f}")
    print(f"Best score      : {best}")
    print(f"Worst score     : {worst}")
    if avg >= 90:
        print("Status          : Excellent")
    elif avg >= 70:
        print("Status          : Good")
    else:
        print("Status          : Needs Improvement")

student_report([95, 87, 91, 89])
