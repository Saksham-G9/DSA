from binary_tree_examples import TreeNode, ALL_TREES


def binary_tree_to_dll(root: TreeNode | None):
    if not root:
        return None

    prev = None
    head = None

    def inorder(node):
        nonlocal prev, head

        if not node:
            return

        inorder(node.left)

        if prev is None:
            head = node
        else:
            prev.right = node
            node.left = prev

        prev = node

        inorder(node.right)

    inorder(root)
    return head


if __name__ == "__main__":
    for name, root in ALL_TREES.items():
        print("---", name, "---")
        (binary_tree_to_dll(root))
        print()
