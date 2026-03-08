from binary_tree_examples import TreeNode, ALL_TREES


def print_binary_tree(node: TreeNode | None):
    if not node:
        return
    print(f"{node.val}: ", end=" ")
    if node.left:
        print(f"L -> {node.left.val}, ", end="")
    else:
        print("L -> None, ", end="")
    if node.right:
        print(f"R ->  {node.right.val}", end="")
    else:
        print("R ->  None", end="")
    print()
    print_binary_tree(node.left)
    print_binary_tree(node.right)


if __name__ == "__main__":
    for name, root in ALL_TREES.items():
        print("---", name, "---")
        print_binary_tree(root)
        print()
