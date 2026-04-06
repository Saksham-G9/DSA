from bisect import bisect_left, bisect_right

arr = [1, 2, 3, 3, 3, 6, 6]


def find_first_and_last_bisect(arr: list[int], k: int):
    left = bisect_left(arr, k)
    print("Left: ", left)
    if left == len(arr) or arr[left] != k:
        return -1, -1
    right = bisect_right(arr, k) - 1
    return left, right


print(find_first_and_last_bisect(arr, 62))
