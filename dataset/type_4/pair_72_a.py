def total_ratings(reviews):
    result = 0
    for item in reviews:
        result = result + item["stars"]
    return result

def average_ratings(reviews):
    count = 0
    total = 0
    for item in reviews:
        count += 1
        total += item["stars"]
    if count == 0:
        return 0
    return total / count

def maximum_ratings(reviews):
    if not reviews:
        return None
    best = reviews[0]
    for item in reviews[1:]:
        if item["stars"] > best["stars"]:
            best = item
    return best

def select_ratings(reviews, minimum):
    selected = []
    for item in reviews:
        if item["stars"] >= minimum:
            selected.append(item)
    return selected

def rating_report(reviews, minimum):
    total = total_ratings(reviews)
    average = average_ratings(reviews)
    best = maximum_ratings(reviews)
    selected = select_ratings(reviews, minimum)
    print(f"Total stars: {total}")
    print(f"Average stars: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_ratings = [{"product": "pen", "stars": 4}, {"product": "bag", "stars": 5}, {"product": "cup", "stars": 3}]
rating_report(data_ratings, 10)
