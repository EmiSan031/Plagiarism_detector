def total_emails(messages):
    return sum(map(lambda entry: entry["size"], messages))

def average_emails(messages):
    values = tuple(entry["size"] for entry in messages)
    return sum(values) / len(values) if values else 0

def maximum_emails(messages):
    return max(messages, key=lambda entry: entry["size"], default=None)

def select_emails(messages, minimum):
    return list(filter(lambda entry: entry["size"] >= minimum, messages))

def email_report(messages, minimum):
    summary = (
        total_emails(messages),
        average_emails(messages),
        maximum_emails(messages),
        select_emails(messages, minimum),
    )
    labels = ("Total size", "Average size", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_emails = [{"sender": "a@x.com", "size": 18}, {"sender": "b@y.com", "size": 9}, {"sender": "c@z.com", "size": 31}]
email_report(data_emails, 10)
