from common import TreeNode, ALL_TREES
from collections import deque


def largestValues(root: TreeNode) -> list[int]:
    res = []
    queue = deque()

    queue.append(root)

    while queue:
        curr_max = float("-inf")
        for _ in range(len(queue)):
            node = queue.popleft()
            curr_max = max(node.data, curr_max)
            for child in node.children:
                queue.append(child)

        res.append(curr_max)

    return res


if __name__ == "__main__":
    for builder in ALL_TREES:
        root = builder()
        print(largestValues(root))
