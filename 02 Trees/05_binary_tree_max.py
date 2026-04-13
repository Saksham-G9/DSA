from binary_tree_examples import TreeNode, ALL_TREES


def binary_tree_max(root: TreeNode | None) -> int:
    if root is None:
        return int(-1e9)

    left_max = binary_tree_max(root.left)
    right_max = binary_tree_max(root.right)

    return max(root.val , left_max , right_max)


if __name__ == "__main__":
    for name, root in ALL_TREES.items():
        print("---", name, "---")
        print(binary_tree_max(root))
        print()
