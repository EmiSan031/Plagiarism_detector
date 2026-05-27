def total_donations(gifts):
    return sum(map(lambda entry: entry["amount"], gifts))

def average_donations(gifts):
    values = tuple(entry["amount"] for entry in gifts)
    return sum(values) / len(values) if values else 0

def maximum_donations(gifts):
    return max(gifts, key=lambda entry: entry["amount"], default=None)

def select_donations(gifts, minimum):
    return list(filter(lambda entry: entry["amount"] >= minimum, gifts))

def donation_report(gifts, minimum):
    summary = (
        total_donations(gifts),
        average_donations(gifts),
        maximum_donations(gifts),
        select_donations(gifts, minimum),
    )
    labels = ("Total amount", "Average amount", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_donations = [{"donor": "A", "amount": 60}, {"donor": "B", "amount": 45}, {"donor": "C", "amount": 90}]
donation_report(data_donations, 10)
