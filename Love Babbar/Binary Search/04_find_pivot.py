def find_pivot(arr: list[int]):
    if not arr:
        raise ValueError("find_pivot() requires a non-empty list")

    start, end = 0, len(arr) - 1

    if arr[start] < arr[end]:
        return arr[start]

    while start < end:
        mid = (start + end) // 2
        if arr[mid] > arr[end]:
            start = mid + 1
        elif arr[mid] < arr[end]:
            end = mid
        else:
            end -= 1

    return arr[start]


arr = [7, 9, 10, 1, 2, 3, 4]
print(find_pivot(arr))
