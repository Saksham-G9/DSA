def search_sorted_matrix(mat: list[list[int]], target: int):

    start_row = 0
    end_row = len(mat) - 1

    while start_row <= end_row:

        mid_row = (start_row + end_row) // 2

        if mat[mid_row][0] <= target <= mat[mid_row][-1]:
            if target in mat[mid_row]:
                return mid_row, mat[mid_row].index(target)

        if mat[mid_row][0] < target:
            start_row = mid_row + 1
        else:
            end_row = mid_row - 1


mat = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
print(search_sorted_matrix(mat, 39))
