def total_ratings(reviews):
    return sum(map(lambda entry: entry["stars"], reviews))

def average_ratings(reviews):
    values = tuple(entry["stars"] for entry in reviews)
    return sum(values) / len(values) if values else 0

def maximum_ratings(reviews):
    return max(reviews, key=lambda entry: entry["stars"], default=None)

def select_ratings(reviews, minimum):
    return list(filter(lambda entry: entry["stars"] >= minimum, reviews))

def rating_report(reviews, minimum):
    summary = (
        total_ratings(reviews),
        average_ratings(reviews),
        maximum_ratings(reviews),
        select_ratings(reviews, minimum),
    )
    labels = ("Total stars", "Average stars", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_ratings = [{"product": "pen", "stars": 4}, {"product": "bag", "stars": 5}, {"product": "cup", "stars": 3}]
rating_report(data_ratings, 10)
