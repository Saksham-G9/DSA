from binary_tree_examples import TreeNode
from print_binary_tree import print_binary_tree


def take_input(node: TreeNode | None):
    if node is None:  # Edge Case
        return

    left = input(f"Enter val of left node of {node.val}: ")
    right = input(f"Enter val of right node of {node.val}: ")
    if left:
        left_node = TreeNode(int(left))
        node.left = left_node
        take_input(left_node)
    if right:
        right_node = TreeNode(int(right))
        node.right = right_node
        take_input(right_node)


root = TreeNode(1)
take_input(root)

print_binary_tree(root)
