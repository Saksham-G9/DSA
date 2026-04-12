from binary_tree_examples import TreeNode


def print_node_at_k(root: TreeNode | None, k: int):
    def _helper(node: TreeNode | None, curr_dis: int):
        if node is None or curr_dis > k:
            return

        _helper(node.left, curr_dis + 1)
        _helper(node.right, curr_dis + 1)

        if curr_dis == k:
            print(node.val, end=" ")

    return _helper(root, 0)


if __name__ == "__main__":
    # Simple test harness
    # Construct tree:
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.right = n6

    print("Nodes at distance 0:", end=" ")
    print_node_at_k(n1, 0)
    print()

    print("Nodes at distance 1:", end=" ")
    print_node_at_k(n1, 1)
    print()

    print("Nodes at distance 2:", end=" ")
    print_node_at_k(n1, 2)
    print()

    print("Nodes at distance 3 (none):", end=" ")
    print_node_at_k(n1, 3)
    print()
