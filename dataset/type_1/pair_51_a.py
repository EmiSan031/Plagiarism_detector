def total_votes(precincts):
    total = 0
    for item in precincts:
        total += item["votes"]
    return total

def average_votes(precincts):
    if not precincts:
        return 0
    return total_votes(precincts) / len(precincts)

def count_high_votes(precincts, minimum):
    count = 0
    for item in precincts:
        if item["votes"] >= minimum:
            count += 1
    return count

def vote_report(precincts, minimum):
    total = total_votes(precincts)
    average = average_votes(precincts)
    high_count = count_high_votes(precincts, minimum)
    print(f"Total votes: {total}")
    print(f"Average votes: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_votes = [{"zone": "N", "votes": 320}, {"zone": "S", "votes": 280}, {"zone": "E", "votes": 410}]
vote_report(records_votes, 10)
