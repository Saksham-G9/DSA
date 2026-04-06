from bisect import bisect_left, bisect_right


def total_occurance(arr: list[int], target: int):
    left = bisect_left(arr, target)

    if left == len(arr) or arr[left] != target:
        return -1

    right = bisect_right(arr, target)

    return right - left

arr = [1, 2, 3, 3, 3, 6, 6]

print(total_occurance(arr, 3))