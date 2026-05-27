def total_hotel(stays):
    return sum(map(lambda entry: entry["nights"], stays))

def average_hotel(stays):
    values = tuple(entry["nights"] for entry in stays)
    return sum(values) / len(values) if values else 0

def maximum_hotel(stays):
    return max(stays, key=lambda entry: entry["nights"], default=None)

def select_hotel(stays, minimum):
    return list(filter(lambda entry: entry["nights"] >= minimum, stays))

def hotel_report(stays, minimum):
    summary = (
        total_hotel(stays),
        average_hotel(stays),
        maximum_hotel(stays),
        select_hotel(stays, minimum),
    )
    labels = ("Total nights", "Average nights", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_hotel = [{"guest": "Iris", "nights": 3}, {"guest": "Leo", "nights": 2}, {"guest": "Noe", "nights": 5}]
hotel_report(data_hotel, 10)
