def total_books(books):
    return sum(map(lambda entry: entry["pages"], books))

def average_books(books):
    values = tuple(entry["pages"] for entry in books)
    return sum(values) / len(values) if values else 0

def maximum_books(books):
    return max(books, key=lambda entry: entry["pages"], default=None)

def select_books(books, minimum):
    return list(filter(lambda entry: entry["pages"] >= minimum, books))

def book_report(books, minimum):
    summary = (
        total_books(books),
        average_books(books),
        maximum_books(books),
        select_books(books, minimum),
    )
    labels = ("Total pages", "Average pages", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_books = [{"title": "Blue", "pages": 210}, {"title": "Green", "pages": 145}, {"title": "Red", "pages": 300}]
book_report(data_books, 10)
