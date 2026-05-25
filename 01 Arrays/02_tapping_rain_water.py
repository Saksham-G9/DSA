from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        res = 0

        max_left_boundary = [0] * n
        max_right_boundary = [0] * n

        # max to the left (excluding current index)
        for i in range(1, n):
            max_left_boundary[i] = max(max_left_boundary[i - 1], height[i - 1])

        # max to the right (excluding current index)
        for i in range(n - 2, -1, -1):
            max_right_boundary[i] = max(max_right_boundary[i + 1], height[i + 1])

        # compute trapped water
        for i in range(n):
            water_level = min(max_left_boundary[i], max_right_boundary[i])
            if water_level > height[i]:
                res += water_level - height[i]

        return res