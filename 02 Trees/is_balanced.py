from binary_tree_examples import TreeNode, ALL_TREES


def is_balanced(root: TreeNode | None):

    def _helper(node):
        if node is None:
            return 0, True

        left_h, left_bal = _helper(node.left)
        if not left_bal:
            return 0, False

        right_h, right_bal = _helper(node.right)
        if not right_bal:
            return 0, False

        if abs(left_h - right_h) > 1:
            return 0, False

        return max(left_h, right_h) + 1, True

    return _helper(root)[1]

if __name__ == "__main__":
    for name, root in ALL_TREES.items():
        print("---", name, "---")
        print(is_balanced(root))
        print()
