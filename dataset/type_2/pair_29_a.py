def neighbors(graph, node):
    if node in graph:
        return graph[node]
    return []

def has_edge(graph, start, end):
    for node in neighbors(graph, start):
        if node == end:
            return True
    return False

def edge_report(graph, start, end):
    connected = has_edge(graph, start, end)
    print(f"{start} -> {end}: {connected}")
    return connected

network = {"a": ["b", "c"], "b": ["d"], "c": []}
edge_report(network, "a", "c")

def node_count(graph):
    count = 0
    for node in graph:
        count += 1
    return count

print(f"Nodes: {node_count(network) if 'network' in globals() else node_count(routes)}")

def describe_sample_size(values):
    size = 0
    for _ in values:
        size += 1
    if size == 0:
        return "empty"
    if size == 1:
        return "single"
    return "multiple"

print(describe_sample_size([1, 2, 3]))
