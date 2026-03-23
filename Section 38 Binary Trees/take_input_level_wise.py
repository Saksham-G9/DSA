from binary_tree_examples import TreeNode
from print_binary_tree import print_binary_tree
from collections import deque


def take_input_level_wise():
    root = TreeNode(int(input("Enter val of root Node: ")))

    queue = deque([root])

    while queue:
        node = queue.popleft()
        left = input(f"Enter val of left node for root {node.val}: ")
        right = input(f"Enter val of right node for root {node.val}: ")

        if left:
            node.left = TreeNode(int(left))
            queue.append(node.left)
        if right:
            node.right = TreeNode(int(right))
            queue.append(node.right)

    return root


if __name__ == "__main__":
    print_binary_tree(take_input_level_wise())
