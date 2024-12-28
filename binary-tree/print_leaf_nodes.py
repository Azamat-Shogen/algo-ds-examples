
class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Recursive solution
def print_leaf_nodes(root):
    if root is None:
        return

    # Base case
    if root.left is None and root.right is None:
        print(root.val, end=', ')
        return

    print_leaf_nodes(root.left)
    print_leaf_nodes(root.right)


def build_tree():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)
    return root

# Test the function
root = build_tree()
print_leaf_nodes(root)