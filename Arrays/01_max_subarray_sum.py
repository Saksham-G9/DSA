def maxSubArray(nums: list[int]):
    max_sum = float("-inf")
    curr_sum = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            max_sum = max(curr_sum, max_sum)
        curr_sum = 0

    return max_sum


def maxSubArray_op(nums: list[int]):

    curr_sum = 0
    max_sum = float("-inf")

    for el in nums:
        curr_sum = curr_sum + el
        max_sum = max(curr_sum, max_sum)
        if curr_sum < 0:
            curr_sum = 0

    return max_sum


nums = [-2, 1]
print(maxSubArray_op(nums))
