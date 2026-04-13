def moveZeroes(nums: list[int]):
    # Stable in-place move: keep non-zero order
    write = 0

    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1

    return nums


arr = [0, 1, 0, 3, 12]
print(moveZeroes(arr))
