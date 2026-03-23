from binary_tree_examples import TreeNode, ALL_TREES


def diameter_binary_tree(node: TreeNode | None) -> int:
    """Return the diameter (number of nodes on longest path) of the tree.

    Uses a helper that returns (height, diameter) for each subtree so the
    algorithm runs in O(n) time.
    """
    diameter = 0

    def _dfs(n: TreeNode | None) -> int:
        nonlocal diameter
        if n is None:
            return 0
        lh = _dfs(n.left)
        rh = _dfs(n.right)
        diameter = max(diameter, lh + rh + 1)
        return max(lh, rh) + 1

    _dfs(node)
    return diameter


if __name__ == "__main__":
    for name, root in ALL_TREES.items():
        print("---", name, "---")
        print(diameter_binary_tree(root))
        print()
