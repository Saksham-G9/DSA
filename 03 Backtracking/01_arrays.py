arr = [-1] * 5


def add_val(arr: list[int], idx: int):

    if idx == len(arr):
        print("Array before backtracking", arr)
        return

    # Work
    arr[idx] = idx + 1

    add_val(arr, idx + 1)

    arr[idx] -= 2


add_val(arr, 0)

print("Array after backtracking", arr)
