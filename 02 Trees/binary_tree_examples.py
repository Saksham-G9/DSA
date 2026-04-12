class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Example binary tree structures (simple -> complex)
# Each function returns the root `TreeNode` for that example.


def single_node():
    # Tree:
    # 1
    return TreeNode(1)


def simple_tree():
    # Tree:
    #   1
    #  / \
    # 2   3
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    return root


def left_skewed():
    # Tree (left skewed):
    #   1
    #  /
    # 2
    # /
    # 3
    n3 = TreeNode(3)
    n2 = TreeNode(2, n3)
    root = TreeNode(1, n2)
    return root


def right_skewed():
    # Tree (right skewed):
    # 1
    #  \
    #   2
    #    \
    #     3
    n3 = TreeNode(3)
    n2 = TreeNode(2, None, n3)
    root = TreeNode(1, None, n2)
    return root


def full_tree():
    # Full binary tree:
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n2 = TreeNode(2, n4, n5)
    n3 = TreeNode(3, None, n6)
    root = TreeNode(1, n2, n3)
    return root


def complete_tree():
    # Complete tree (filled left-to-right):
    #       1
    #      / \
    #     2   3
    #    / \  /
    #   4  5 6
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n2 = TreeNode(2, n4, n5)
    n3 = TreeNode(3, n6, None)
    root = TreeNode(1, n2, n3)
    return root


def perfect_tree_depth3():
    # Perfect binary tree of depth 3:
    #        1
    #      /   \
    #     2     3
    #    / \   / \
    #   4  5  6   7
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n2 = TreeNode(2, n4, n5)
    n3 = TreeNode(3, n6, n7)
    root = TreeNode(1, n2, n3)
    return root


def complex_tree():
    # More complex, unbalanced tree:
    #         10
    #        /  \
    #       5    15
    #      / \     \
    #     3   7     20
    #        / \    /
    #       6   9  17
    n3 = TreeNode(3)
    n6 = TreeNode(6)
    n9 = TreeNode(9)
    n7 = TreeNode(7, n6, n9)
    n5 = TreeNode(5, n3, n7)
    n17 = TreeNode(17)
    n20 = TreeNode(20, n17, None)
    n15 = TreeNode(15, None, n20)
    root = TreeNode(10, n5, n15)
    return root


def get_all_examples():
    return {
        "single_node": single_node(),
        "simple_tree": simple_tree(),
        "left_skewed": left_skewed(),
        "right_skewed": right_skewed(),
        "full_tree": full_tree(),
        "complete_tree": complete_tree(),
        "perfect_tree_depth3": perfect_tree_depth3(),
        "complex_tree": complex_tree(),
    }


ALL_TREES = get_all_examples()

__all__ = [
    "single_node",
    "simple_tree",
    "left_skewed",
    "right_skewed",
    "full_tree",
    "complete_tree",
    "perfect_tree_depth3",
    "complex_tree",
    "get_all_examples",
    "ALL_TREES",
]
