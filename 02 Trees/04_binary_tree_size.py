from binary_tree_examples import TreeNode, ALL_TREES
def size(root: TreeNode | None):

    if root is None:
        return 0
    
    left_size = size(root.left)
    right_size = size(root.right)

    return 1 + left_size + right_size

if __name__ == "__main__":
    for name, root in ALL_TREES.items():
        print("---", name, "---")
        print(size(root))
        print()

