def neighbors(graph, node):
    if node in graph:
        return graph[node]
    return []

def has_edge(graph, start, end):
    for node in neighbors(graph, start):
        if node == end:
            return True
    return False

def degree(graph, node):
    count = 0
    for item in neighbors(graph, node):
        count += 1
    return count

def edge_report(graph, start, end):
    connected = has_edge(graph, start, end)
    count = degree(graph, start)
    print(f"{start} -> {end}: {connected}")
    print(f"Neighbors from {start}: {count}")
    return connected

network = {"a": ["b", "c"], "b": ["d"], "c": []}
edge_report(network, "a", "c")

def node_count(graph):
    count = 0
    for node in graph:
        count += 1
    return count

print(f"Nodes: {node_count(network) if 'network' in globals() else node_count(routes)}")
