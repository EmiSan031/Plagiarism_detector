def total_movies(movies):
    total = 0
    for item in movies:
        total += item["minutes"]
    return total

def average_movies(movies):
    if not movies:
        return 0
    return total_movies(movies) / len(movies)

def high_movies(movies, minimum):
    selected = []
    for item in movies:
        if item["minutes"] >= minimum:
            selected.append(item)
    return selected

def movie_report(movies, minimum):
    total = total_movies(movies)
    average = average_movies(movies)
    selected = high_movies(movies, minimum)
    print(f"Records         : {movies}")
    print(f"Total minutes  : {total}")
    print(f"Average minutes: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_movies = [{"title": "One", "minutes": 95, "rating": 8}, {"title": "Two", "minutes": 122, "rating": 7}]
movie_report(example_movies, 10)
