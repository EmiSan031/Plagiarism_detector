def total_books(books):
    total = 0
    for item in books:
        total += item["pages"]
    return total

def average_books(books):
    if not books:
        return 0
    return total_books(books) / len(books)

def high_books(books, minimum):
    selected = []
    for item in books:
        if item["pages"] >= minimum:
            selected.append(item)
    return selected

def book_report(books, minimum):
    total = total_books(books)
    average = average_books(books)
    selected = high_books(books, minimum)
    print(f"Records         : {books}")
    print(f"Total pages  : {total}")
    print(f"Average pages: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_books = [{"title": "Blue", "pages": 210, "chapters": 12}, {"title": "Green", "pages": 145, "chapters": 9}]
book_report(example_books, 10)
