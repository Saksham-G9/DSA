from binary_tree_examples import TreeNode, ALL_TREES


def height(node: TreeNode | None):
    if node is None:
        return 0

    left_h = height(node.left)
    right_h = height(node.right)

    return max(left_h, right_h) + 1


if __name__ == "__main__":
    for name, root in ALL_TREES.items():
        print("---", name, "---")
        print(height(root))
        print()
