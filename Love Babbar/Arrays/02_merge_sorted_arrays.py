def merge_sorted_arrays(arr: list[int], m: int, arr2: list[int], n: int):
    m = m - 1
    n = n - 1
    len_arr = len(arr) - 1
    while m >= 0 and n >= 0:
        if arr[m] > arr2[n]:
            arr[len_arr] = arr[m]
            m -= 1
        else:
            arr[len_arr] = arr2[n]
            n -= 1
        len_arr -= 1


arr1 = [1, 2, 3, 0, 0, 0]
arr2 = [2, 5, 6]

merge_sorted_arrays(arr1, 3, arr2, 3)

print(arr1)
