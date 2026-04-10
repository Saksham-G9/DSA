def search_rotated_sorted(arr: list[int], target: int):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid

        # Left half sorted
        if arr[start] <= arr[mid]:
            if arr[start] <= target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

        # Right half sorted
        else:
            if arr[mid] < target <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1