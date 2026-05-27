def total_hotel(stays):
    result = 0
    for item in stays:
        result = result + item["nights"]
    return result

def average_hotel(stays):
    count = 0
    total = 0
    for item in stays:
        count += 1
        total += item["nights"]
    if count == 0:
        return 0
    return total / count

def maximum_hotel(stays):
    if not stays:
        return None
    best = stays[0]
    for item in stays[1:]:
        if item["nights"] > best["nights"]:
            best = item
    return best

def select_hotel(stays, minimum):
    selected = []
    for item in stays:
        if item["nights"] >= minimum:
            selected.append(item)
    return selected

def hotel_report(stays, minimum):
    total = total_hotel(stays)
    average = average_hotel(stays)
    best = maximum_hotel(stays)
    selected = select_hotel(stays, minimum)
    print(f"Total nights: {total}")
    print(f"Average nights: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_hotel = [{"guest": "Iris", "nights": 3}, {"guest": "Leo", "nights": 2}, {"guest": "Noe", "nights": 5}]
hotel_report(data_hotel, 10)
