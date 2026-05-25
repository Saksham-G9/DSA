class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways = 0

        def _helper(i, j):

            # Base Case
            if i == m - 1 and j == n - 1:
                nonlocal ways
                ways += 1

            # Right Choice
            if i < m - 1:
                _helper(i + 1, j)
            # Down Choice
            if j < n - 1:
                _helper(i, j + 1)

        _helper(0, 0)
        return ways


sol = Solution()
print(sol.uniquePaths(3, 7))
