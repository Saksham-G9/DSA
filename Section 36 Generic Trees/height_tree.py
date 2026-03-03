from collections import deque

from common import ALL_TREES
from tree_node import TreeNode

def height_tree(root: TreeNode) -> int:
    if root is None:
        return 0

    q = deque([root])
    height = 0

    while q:
        height += 1
        for _ in range(len(q)):
            node = q.popleft()
            for child in node.children:
                q.append(child)

    return height


if __name__ == "__main__":
    for builder in ALL_TREES:
        root = builder()
        print(height_tree(root))
