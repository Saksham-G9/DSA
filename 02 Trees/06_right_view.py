from collections import deque

from binary_tree_examples import TreeNode, ALL_TREES


def rightSideView(root: TreeNode | None) -> list[int] | None:
    if root is None:
        return

    queue = deque([root])

    result = []

    while queue:
        len_queue = len(queue)
        
        # Printing right most node of level
        result.append(queue[-1].val)
        
        for _ in range(len_queue):
            curr_node = queue.popleft()

            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)

    return result


if __name__ == "__main__":
    for name, root in ALL_TREES.items():
        print("---", name, "---")
        print(rightSideView(root))
        print()
