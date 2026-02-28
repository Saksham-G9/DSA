class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid
        if left == 0:
            return k
        return arr[left - 1] + (k - (arr[left - 1] - (left - 1) - 1))
        # return k + left


arr = [2, 3, 4, 7, 11]
k = 5

sol = Solution()
print(sol.findKthPositive(arr, k))
