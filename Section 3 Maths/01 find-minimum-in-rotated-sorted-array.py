class Solution:
    def findMin(self, arr: list[int]) -> int:
        # Check if array is non rotated
        if arr[0] < arr[-1]:
            return arr[0]


        start, end = 0, len(arr) - 1
        ans = arr[0]

        while start <= end:

            mid = (start + end) // 2

            if arr[mid] < arr[0]:
                ans = arr[mid]
                end = mid - 1
            else:
                start = mid + 1

        return ans