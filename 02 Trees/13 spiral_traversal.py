from binary_tree_examples import ALL_TREES, TreeNode

from collections import deque


def spiral_traversal(root: TreeNode):
    if not root:
        return

    queue = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if not left_to_right:
            level.reverse()

        print(*level)
        left_to_right = not left_to_right


if __name__ == "__main__":
    for name, root in ALL_TREES.items():
        print("---", name, "---")
        (spiral_traversal(root))
        print()
