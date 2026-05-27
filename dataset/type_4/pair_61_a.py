def total_books(books):
    result = 0
    for item in books:
        result = result + item["pages"]
    return result

def average_books(books):
    count = 0
    total = 0
    for item in books:
        count += 1
        total += item["pages"]
    if count == 0:
        return 0
    return total / count

def maximum_books(books):
    if not books:
        return None
    best = books[0]
    for item in books[1:]:
        if item["pages"] > best["pages"]:
            best = item
    return best

def select_books(books, minimum):
    selected = []
    for item in books:
        if item["pages"] >= minimum:
            selected.append(item)
    return selected

def book_report(books, minimum):
    total = total_books(books)
    average = average_books(books)
    best = maximum_books(books)
    selected = select_books(books, minimum)
    print(f"Total pages: {total}")
    print(f"Average pages: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_books = [{"title": "Blue", "pages": 210}, {"title": "Green", "pages": 145}, {"title": "Red", "pages": 300}]
book_report(data_books, 10)
