def total_emails(messages):
    result = 0
    for item in messages:
        result = result + item["size"]
    return result

def average_emails(messages):
    count = 0
    total = 0
    for item in messages:
        count += 1
        total += item["size"]
    if count == 0:
        return 0
    return total / count

def maximum_emails(messages):
    if not messages:
        return None
    best = messages[0]
    for item in messages[1:]:
        if item["size"] > best["size"]:
            best = item
    return best

def select_emails(messages, minimum):
    selected = []
    for item in messages:
        if item["size"] >= minimum:
            selected.append(item)
    return selected

def email_report(messages, minimum):
    total = total_emails(messages)
    average = average_emails(messages)
    best = maximum_emails(messages)
    selected = select_emails(messages, minimum)
    print(f"Total size: {total}")
    print(f"Average size: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_emails = [{"sender": "a@x.com", "size": 18}, {"sender": "b@y.com", "size": 9}, {"sender": "c@z.com", "size": 31}]
email_report(data_emails, 10)
