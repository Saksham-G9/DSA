from binary_tree_examples import TreeNode, ALL_TREES


def isBalanced(root: TreeNode | None) -> bool:
    def _height(node: TreeNode | None) -> int:
        if node is None:
            return 0

        left_height = _height(node.left)
        if left_height == -1:
            return -1

        right_height = _height(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

    return _height(root) != -1


if __name__ == "__main__":
    for name, root in ALL_TREES.items():
        print("---", name, "---")
        print(isBalanced(root))
        print()
