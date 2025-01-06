from print_leaf_nodes import build_tree
from collections import deque


def print_node_rows(root):
    if not root:
        return []

    dq = deque([root])
    res = []

    while dq:
        level_size = len(dq)  # Number of nodes at the current Level
        level = []

        for _ in range(level_size):
            node = dq.popleft()
            level.append(node.val)
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)

        res.append(level)

    return res


tree_root = build_tree()

print(print_node_rows(tree_root))
# result should print out
# 1
# 2 3
# 4 5 6 7


