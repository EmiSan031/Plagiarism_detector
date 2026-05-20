def neighbors(graph, node):
    return graph.get(node, [])

def has_edge(graph, start, end):
    return end in neighbors(graph, start)

def edge_report(graph, start, end):
    connected = has_edge(graph, start, end)
    print("{} -> {}: {}".format(start, end, connected))
    return connected

network = {"a": ["b", "c"], "b": ["d"], "c": []}
edge_report(network, "a", "c")

def node_count(graph):
    return len(graph)

print("Nodes:", node_count(network))

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
