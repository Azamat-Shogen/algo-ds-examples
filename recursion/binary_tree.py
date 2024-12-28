
class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert_node(head, data):
    # If head is empty // base-case - insert the node at the leaf level ( or root if empty )
    if head is None:
        head = BinaryTreeNode(data)
        return head

    if head.val < data:
        head.right = insert_node(head.right, data)
    else:
        head.left = insert_node(head.left, data)

    return head


# Create the root of the tree
root = BinaryTreeNode(10)

# Insert values into tree
insert_node(root, 5)
insert_node(root, 15)
insert_node(root, 3)
insert_node(root, 7)
insert_node(root, 12)
insert_node(root, 18)


# Helper function to print the tree ( in-order traversal )
def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.left)  # Visit the root
    print(node.val, end=" ")  # Traverse the left subtree
    in_order_traversal(node.right)  # Traverse the right subtree


def pre_order_traversal(node):
    if node is None:
        return
    print(node.val, end=" ")
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)


in_order_traversal(root)
print('\n*')
pre_order_traversal(root)





