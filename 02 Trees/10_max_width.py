from collections import deque

from binary_tree_examples import ALL_TREES, TreeNode


def max_width(root: TreeNode):
    if root is None:
        return 0

    res_max_width = 1

    queue = deque([root])

    while queue:

        len_queue = len(queue)
        res_max_width = max(res_max_width, len_queue)

        for _ in range(len_queue):
            curr_node = queue.popleft()
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
    return res_max_width

if __name__ == "__main__":
    for name, root in ALL_TREES.items():
        print("---", name, "---")
        print(max_width(root))
        print()