def undirected_path_dfs(edges, node_a, node_b):
    graph = build_graph(edges)
    return has_path(graph, node_a, node_b)


def has_path(graph, src, dst, visited=None):
    if visited is None:
        visited = set()

    if src in visited:
        return False

    if src == dst:
        return True

    visited.add(src)

    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst, visited):  # Fixed argument order
            return True

    return False


def build_graph(edges_list):
    obj = {}
    for row in edges_list:
        a, b = row[0], row[1]
        if a not in obj:
            obj[a] = []
        if b not in obj:
            obj[b] = []

        obj[a].append(b)
        obj[b].append(a)

    return obj


edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n'],
]

print(undirected_path_dfs(edges, 'i', 'j'))  # True
print(undirected_path_dfs(edges, 'i', 'o'))  # False
