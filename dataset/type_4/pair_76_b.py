def total_movies(movies):
    return sum(map(lambda entry: entry["minutes"], movies))

def average_movies(movies):
    values = tuple(entry["minutes"] for entry in movies)
    return sum(values) / len(values) if values else 0

def maximum_movies(movies):
    return max(movies, key=lambda entry: entry["minutes"], default=None)

def select_movies(movies, minimum):
    return list(filter(lambda entry: entry["minutes"] >= minimum, movies))

def movie_report(movies, minimum):
    summary = (
        total_movies(movies),
        average_movies(movies),
        maximum_movies(movies),
        select_movies(movies, minimum),
    )
    labels = ("Total minutes", "Average minutes", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_movies = [{"title": "One", "minutes": 95}, {"title": "Two", "minutes": 122}, {"title": "Three", "minutes": 88}]
movie_report(data_movies, 10)
