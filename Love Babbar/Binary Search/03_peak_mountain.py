def peak_mountain_index(arr: list[int]) -> int:
    if not arr:
        return -1
    start, end = 0, len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < arr[mid + 1]:
            start = mid + 1
        else:
            end = mid
    return start


arr = [0, 10,11, 5, 2]
print(peak_mountain_index(arr))
