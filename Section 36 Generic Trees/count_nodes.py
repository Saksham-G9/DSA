from common import ALL_TREES
from tree_node import TreeNode


def count_nodes(root: TreeNode):
    count = 0

    def _helper(node: TreeNode) -> None:
        nonlocal count
        count += 1

        for child in node.children:
            _helper(child)
    
    _helper(root)

    return count
if __name__ == "__main__":
    for builder in ALL_TREES:
        root = builder()
        print(count_nodes(root))
