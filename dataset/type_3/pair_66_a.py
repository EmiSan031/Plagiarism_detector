def total_hotel(stays):
    total = 0
    for item in stays:
        total += item["nights"]
    return total

def average_hotel(stays):
    if not stays:
        return 0
    return total_hotel(stays) / len(stays)

def high_hotel(stays, minimum):
    selected = []
    for item in stays:
        if item["nights"] >= minimum:
            selected.append(item)
    return selected

def hotel_report(stays, minimum):
    total = total_hotel(stays)
    average = average_hotel(stays)
    selected = high_hotel(stays, minimum)
    print(f"Records         : {stays}")
    print(f"Total nights  : {total}")
    print(f"Average nights: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_hotel = [{"guest": "Iris", "nights": 3, "rate": 90}, {"guest": "Leo", "nights": 2, "rate": 110}]
hotel_report(example_hotel, 10)
