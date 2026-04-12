def reverse_after_pos(arr: list[int], k: int):
    start = k
    end = len(arr) - 1

    while start < end:
        temp = arr[start]

        arr[start] = arr[end]
        arr[end] = temp

        start += 1
        end -= 1

    return arr


arr = [1, 2, 3, 4, 5, 6]
print(arr)
reverse_after_pos(arr, 4)
print(arr)

