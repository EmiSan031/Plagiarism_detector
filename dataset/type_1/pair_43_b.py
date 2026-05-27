# Type I clone: only comments and whitespace differ.

def total_badges(members):
    total = 0
    for item in members:
        total += item["badges"]
    return total


# Same function body as the original fragment.
def average_badges(members):
    if not members:
        return 0
    return total_badges(members) / len(members)


# Same function body as the original fragment.
def count_high_badges(members, minimum):
    count = 0
    for item in members:
        if item["badges"] >= minimum:
            count += 1
    return count


# Same function body as the original fragment.
def badge_report(members, minimum):
    total = total_badges(members)
    average = average_badges(members)
    high_count = count_high_badges(members, minimum)
    print(f"Total badges: {total}")
    print(f"Average badges: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_badges = [{"name": "Paz", "badges": 4}, {"name": "Sol", "badges": 7}, {"name": "Rui", "badges": 3}]
badge_report(records_badges, 10)
