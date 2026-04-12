from collections import deque

from binary_tree_examples import TreeNode, ALL_TREES


def level_order_traversal(root: TreeNode):
    if root is None:
        return

    queue = deque([root])

    while queue:
        curr_node = queue.popleft()
        print(curr_node.val, end=": ")
        if curr_node.left:
            queue.append(curr_node.left)
        if curr_node.right:
            queue.append(curr_node.right)

        len_queue = len(queue)

        for _ in range(len_queue):
            node = queue.popleft()
            print(node.val, end=", ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
if __name__ == "__main__":
    for name, root in ALL_TREES.items():
        print("---", name, "---")
        level_order_traversal(root)
        print()
