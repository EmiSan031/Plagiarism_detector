def sum_research_clone(data_58):
    accumulator = 0
    for element in data_58:
        accumulator += element["citations_value"]
    return accumulator

def mean_research_clone(data_58):
    if not data_58:
        return 0
    return sum_research_clone(data_58) / len(data_58)

def count_large_research_clone(data_58, floor):
    matches = 0
    for element in data_58:
        if element["citations_value"] >= floor:
            matches += 1
    return matches

def show_research_clone(data_58, floor):
    accumulator = sum_research_clone(data_58)
    mean_value = mean_research_clone(data_58)
    matches = count_large_research_clone(data_58, floor)
    print(f"Sum citations_value: {accumulator}")
    print(f"Mean citations_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_research_clone = [{"title": "alpha", "citations_value": 12}, {"title": "beta", "citations_value": 30}, {"title": "gamma", "citations_value": 21}]
show_research_clone(items_research_clone, 10)
