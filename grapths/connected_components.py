
def connected_component_count(g):
    visited = set()
    count = 0
    for node in g:
        if explore(g, node, visited) is True:
            count += 1

    return count


def explore(g, curr_node, visited):

    if curr_node in visited:
        return False

    visited.add(curr_node)

    # once we visit all neighbors we've explored all neighbors and return True
    for neighbor in g[curr_node]:
        explore(g, neighbor, visited)

    return True


def largest_component(g):
    visited = set()
    longest = 0

    for node in g:
        count = explore_size(g, node, visited)
        longest = max(longest, count)

    return longest


def explore_size(g, node, visited):
    if node in visited:
        return 0

    visited.add(node)
    size = 1

    for neighbor in g[node]:
        size += explore_size(g, neighbor, visited)

    return size


# Adjacency list
graph1 = {
    3: [],
    4: [6],
    6: [4, 5, 7, 8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1],
}
graph2 = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
}

# print(connected_component_count(graph)) # 3
assert connected_component_count(graph1) == 3, f"Expected the result to be: 3 but got: {connected_component_count(graph1)}"
assert connected_component_count(graph2) == 2, f"Expected the result to be: 3 but got: {connected_component_count(graph2)}"

assert largest_component(graph2) == 4, f"Expected the result to be: 4 but got: {largest_component(graph2)}"
