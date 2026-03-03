from collections import deque
from tree_node import TreeNode


def level_wise_input() -> TreeNode:

    queue = deque()

    data = int(input("Enter the root node value: "))

    rootNode = TreeNode(data)

    queue.append(rootNode)

    while queue:
        root = queue.popleft()

        data = int(input(f"Enter the number of children for node {root.data}: "))

        for i in range(int(data)):
            val = input(f"Enter value of child {i + 1} for node {root.data}: ")
            node = TreeNode(int(val))
            queue.append(node)
            root.children.append(node)
    
    return rootNode

if __name__ == "__main__":
    root = level_wise_input()
    root.print_tree()