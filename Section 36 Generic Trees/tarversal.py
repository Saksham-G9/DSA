from common import TreeNode, ALL_TREES


def pre_order_traversal(root: TreeNode):
    if not root:
        return root
    print(root.data, end=" ")

    for child in root.children:
        pre_order_traversal(child)


def post_order_traversal(root: TreeNode):
    if not root:
        return root

    for child in root.children:
        post_order_traversal(child)
    print(root.data, end=" ")


if __name__ == "__main__":
    for builder in ALL_TREES:
        root = builder()
        print("Pre: ")
        pre_order_traversal(root)
        print("\nPost: ")
        post_order_traversal(root)
        print()
