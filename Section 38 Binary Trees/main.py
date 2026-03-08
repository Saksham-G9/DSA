from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque()

        queue.append(root)

        while queue:
            curr_max = float("-inf")
            for _ in range(len(queue)):
                node = queue.popleft()
                curr_max = max(node.val, curr_max)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(curr_max)

        return res


root = TreeNode(1)

node1 = TreeNode(3)
node2 = TreeNode(2)
node3 = TreeNode(5)
node4 = TreeNode(3)
node5 = TreeNode(9)

root.left = node1
root.right = node2

node1.left = node3
node1.right = node4

node2.right = node5
if __name__ == "__main__":
    sol = Solution()
    print(sol.largestValues(root))