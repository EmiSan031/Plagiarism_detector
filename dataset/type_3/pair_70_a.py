def total_emails(messages):
    total = 0
    for item in messages:
        total += item["size"]
    return total

def average_emails(messages):
    if not messages:
        return 0
    return total_emails(messages) / len(messages)

def high_emails(messages, minimum):
    selected = []
    for item in messages:
        if item["size"] >= minimum:
            selected.append(item)
    return selected

def email_report(messages, minimum):
    total = total_emails(messages)
    average = average_emails(messages)
    selected = high_emails(messages, minimum)
    print(f"Records         : {messages}")
    print(f"Total size  : {total}")
    print(f"Average size: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_emails = [{"sender": "a@x.com", "size": 18, "attachments": 1}, {"sender": "b@y.com", "size": 9, "attachments": 0}]
email_report(example_emails, 10)
