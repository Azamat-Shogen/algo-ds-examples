from collections import deque


# undirected graph

# DFS
def has_path_dfs(g, src, dst):
    if src == dst:
        return True

    for neighbor in g[src]:
        if has_path_dfs(g, neighbor, dst):  # Recursive call to check if a path exists
            return True

    return False


def has_path_bfs(g, src, dst):
    dq = deque([src])

    while dq:
        node = dq.popleft()
        if node == dst:
            return True
        for neighbor in g[node]:
            dq.append(neighbor)

    return False


def has_path_dfs_cached(g, src, dst, visited=None):
    if visited is None:
        visited = set()
    if src == dst:
        return True
    if src in visited:
        return False

    visited.add(src)
    for neighbor in g[src]:
        if has_path_dfs_cached(g, neighbor, dst, visited):
            return True

    return False


def has_path_bfs_cached(g, src, dst, visited=None):
    if visited is None:
        visited = set()
    if src == dst:
        return True
    if src in visited:
        return False

    visited.add(src)
    dq = deque([src])

    while dq:
        node = dq.popleft()
        for neighbor in g[node]:
            if neighbor == dst:
                return True
            if neighbor not in visited:
                visited.add(neighbor)
                dq.append(neighbor)

    return False


graph_no_cycle = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

graph_with_cycle = {
    'a': ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a', 'e'],
    'd': ['b'],
    'e': ['c'],
}

print(has_path_dfs(graph_no_cycle, 'f', 'k'))  # True
print(has_path_bfs(graph_no_cycle, 'f', 'k'))  # True

# print(has_path_dfs(graph_with_cycle, 'a', 'e'))  # will cause infinite loop


print(has_path_dfs_cached(graph_with_cycle, 'a', 'e'))  # True
print(has_path_dfs_cached(graph_with_cycle, 'a', 'f'))  # False

print(has_path_bfs_cached(graph_with_cycle, 'a', 'e'))  # True
print(has_path_bfs_cached(graph_with_cycle, 'a', 'f'))  # False

