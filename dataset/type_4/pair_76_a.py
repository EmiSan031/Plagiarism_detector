def total_movies(movies):
    result = 0
    for item in movies:
        result = result + item["minutes"]
    return result

def average_movies(movies):
    count = 0
    total = 0
    for item in movies:
        count += 1
        total += item["minutes"]
    if count == 0:
        return 0
    return total / count

def maximum_movies(movies):
    if not movies:
        return None
    best = movies[0]
    for item in movies[1:]:
        if item["minutes"] > best["minutes"]:
            best = item
    return best

def select_movies(movies, minimum):
    selected = []
    for item in movies:
        if item["minutes"] >= minimum:
            selected.append(item)
    return selected

def movie_report(movies, minimum):
    total = total_movies(movies)
    average = average_movies(movies)
    best = maximum_movies(movies)
    selected = select_movies(movies, minimum)
    print(f"Total minutes: {total}")
    print(f"Average minutes: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_movies = [{"title": "One", "minutes": 95}, {"title": "Two", "minutes": 122}, {"title": "Three", "minutes": 88}]
movie_report(data_movies, 10)
