from binary_tree_examples import TreeNode, ALL_TREES


def pre_order(root: TreeNode | None):
    if root is None:
        return

    print(root.val, end=" ")

    pre_order(root.left)
    pre_order(root.right)


def post_order(root: TreeNode | None):
    if root is None:
        return

    post_order(root.left)
    post_order(root.right)
    print(root.val, end=" ")


def in_order(root: TreeNode | None):
    if root is None:
        return

    in_order(root.left)
    print(root.val, end=" ")
    in_order(root.right)


if __name__ == "__main__":
    for name, root in ALL_TREES.items():
        print("---", name, "---")
        in_order(root)
        print()
