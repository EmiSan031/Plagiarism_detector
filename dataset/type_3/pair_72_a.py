def total_ratings(reviews):
    total = 0
    for item in reviews:
        total += item["stars"]
    return total

def average_ratings(reviews):
    if not reviews:
        return 0
    return total_ratings(reviews) / len(reviews)

def high_ratings(reviews, minimum):
    selected = []
    for item in reviews:
        if item["stars"] >= minimum:
            selected.append(item)
    return selected

def rating_report(reviews, minimum):
    total = total_ratings(reviews)
    average = average_ratings(reviews)
    selected = high_ratings(reviews, minimum)
    print(f"Records         : {reviews}")
    print(f"Total stars  : {total}")
    print(f"Average stars: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_ratings = [{"product": "pen", "stars": 4, "votes": 12}, {"product": "bag", "stars": 5, "votes": 7}]
rating_report(example_ratings, 10)
