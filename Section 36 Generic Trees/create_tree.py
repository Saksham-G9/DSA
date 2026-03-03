from tree_node import TreeNode


def create_tree(root: TreeNode):
    data = input(f"Enter no of children for node {root.data}: ")

    for i in range(int(data)):
        val = input(f"Enter val of {i + 1} child: ")
        node = TreeNode(int(val))
        root.children.append(node)

    for child in root.children:
        create_tree(child)


if __name__ == "__main__":
    root = TreeNode(1)

    create_tree(root)
    root.print_tree()
