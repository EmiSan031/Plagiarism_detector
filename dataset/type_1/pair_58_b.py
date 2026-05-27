# Type I clone: only comments and whitespace differ.

def total_research(papers):
    total = 0
    for item in papers:
        total += item["citations"]
    return total


# Same function body as the original fragment.
def average_research(papers):
    if not papers:
        return 0
    return total_research(papers) / len(papers)


# Same function body as the original fragment.
def count_high_research(papers, minimum):
    count = 0
    for item in papers:
        if item["citations"] >= minimum:
            count += 1
    return count


# Same function body as the original fragment.
def research_report(papers, minimum):
    total = total_research(papers)
    average = average_research(papers)
    high_count = count_high_research(papers, minimum)
    print(f"Total citations: {total}")
    print(f"Average citations: {average:.2f}")
    print(f"High records: {high_count}")
    return total, average, high_count

records_research = [{"title": "alpha", "citations": 12}, {"title": "beta", "citations": 30}, {"title": "gamma", "citations": 21}]
research_report(records_research, 10)
