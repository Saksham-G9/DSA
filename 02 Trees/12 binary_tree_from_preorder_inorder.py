from binary_tree_examples import TreeNode, print_tree_level_order


def binary_tree_from_preorder_inorder(preorder: list[int], inorder: list[int]):
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    idx = inorder.index(root_val)

    left_preorder = preorder[1 : idx + 1]
    right_preorder = preorder[idx + 1 :]

    left_inorder = inorder[:idx]
    right_inorder = inorder[idx + 1 :]

    node = TreeNode(root_val)
    node.left = binary_tree_from_preorder_inorder(left_preorder, left_inorder)
    node.right = binary_tree_from_preorder_inorder(right_preorder, right_inorder)

    return node


inorder = [20, 10, 30]
preorder = [10, 20, 30]

root = binary_tree_from_preorder_inorder(preorder, inorder)

print_tree_level_order(root)
