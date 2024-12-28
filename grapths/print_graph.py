from collections import deque

"""
One directed graph
"""


def depth_first_traversal(g, source):
    # TODO: for dfs we use stack
    stack = [source]
    res = ""
    while stack:
        node = stack.pop()
        res += node
        for neighbor in g[node]:
            stack.append(neighbor)

    return "->".join([x for x in res])


def depth_first_recursive_traversal(g, source, res=""):
    # TODO: dfs recursive version
    res += source
    for neighbor in g[source]:
        depth_first_recursive_traversal(g, neighbor, res)

    return "->".join([x for x in res])


def depth_first_recursive_traversal(g, source):
    # TODO: dfs recursive version
    print(source, end="->")
    for n in g[source]:
        depth_first_recursive_traversal(g, n)


def depth_first_recursive_traversal_cached(g, source):

    def dfs(node, visited, result):
        visited.add(node)  # Mark the node as visited
        result.append(node)  # append the node to the result list

        # Recursively visit all neighbors
        for n in g[node]:
            if n not in visited:
                dfs(n, visited, result)

        return result

    res = dfs(source, set(), [])
    return "->".join(str(x) for x in res)


def breadth_first_traversal(g, source):
    # TODO: for bfs we use queue
    dq = deque([source])
    res = ""
    while dq:
        node = dq.popleft()
        res += node

        for neighbor in g[node]:
            dq.append(neighbor)

    return "->".join([x for x in res])


graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

# print(depth_first_traversal(graph, 'a'))
# print(breadth_first_traversal(graph, 'a'))

# print(depth_first_recursive_traversal(graph, 'a'))
# print(depth_first_recursive_traversal_cached(graph, 'a'))

assert depth_first_traversal(graph, 'a') == 'a->b->d->f->c->e', ""
assert breadth_first_traversal(graph, 'a') == 'a->c->b->e->d->f', ""
assert depth_first_recursive_traversal_cached(graph, 'a') == 'a->c->e->b->d->f', ""
