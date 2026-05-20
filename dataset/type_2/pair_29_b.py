def adjacent_nodes(map_data, source):
    if source in map_data:
        return map_data[source]
    return []

def contains_link(map_data, source, target):
    for candidate in adjacent_nodes(map_data, source):
        if candidate == target:
            return True
    return False

def link_report(map_data, source, target):
    found = contains_link(map_data, source, target)
    print(f"{source} reaches {target}: {found}")
    return found

routes = {"home": ["shop", "park"], "shop": ["bank"], "park": []}
link_report(routes, "home", "park")

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
