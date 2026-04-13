from collections import deque

from binary_tree_examples import TreeNode, ALL_TREES


def left_view(root: TreeNode | None) -> list[int] | None:
    if root is None:
        return

    queue = deque([root])

    result = []

    while queue:
        len_queue = len(queue)
        
        # Printing left most node of level
        result.append(queue[0].val)

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
        print(left_view(root))
        print()
