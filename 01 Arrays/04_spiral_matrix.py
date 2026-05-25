from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []

    row_start, row_end = 0, len(matrix) - 1
    col_start, col_end = 0, len(matrix[0]) - 1

    res = []

    while row_start <= row_end and col_start <= col_end:

        # Top row
        for c in range(col_start, col_end + 1):
            res.append(matrix[row_start][c])

        # Right column
        for r in range(row_start + 1, row_end + 1):
            res.append(matrix[r][col_end])

        # Bottom row
        if row_start < row_end:
            for c in range(col_end - 1, col_start - 1, -1):
                res.append(matrix[row_end][c])

        # Left column
        if col_start < col_end:
            for r in range(row_end - 1, row_start, -1):
                res.append(matrix[r][col_start])

        row_start += 1
        row_end -= 1
        col_start += 1
        col_end -= 1

    return res

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

spiralOrder(matrix)
