from binary_tree_examples import TreeNode, ALL_TREES


def is_balanced(root: TreeNode | None) -> bool:
    """Return True if the tree is height-balanced, else False.

    Uses a helper that returns (height, is_balanced).
    """

    if root is None:
        return True

    def _helper(node: TreeNode | None) -> tuple[int, bool]:
        if node is None:
            return 0, True

        left_height, left_is_balanced = _helper(node.left)
        right_height, right_is_balanced = _helper(node.right)

        curr_height = max(left_height, right_height) + 1
        is_bal = (
            left_is_balanced and right_is_balanced and
            abs(left_height - right_height) <= 1
        )
        return curr_height, is_bal

    return _helper(root)[1]


if __name__ == "__main__":
    for name, root in ALL_TREES.items():
        print("---", name, "---")
        print(is_balanced(root))
        print()
