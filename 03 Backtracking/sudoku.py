from typing import List

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def is_valid(row: int, col: int, num: str):

            # Row Check
            if num in board[row]:
                return False

            # Column Check
            for i in range(9):
                if board[i][col] == num:
                    return False

            # 3x3 Grid Check
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3

            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False

            return True

        def _helper(row: int, col: int):

            # Move to next row
            if col == 9:
                row += 1
                col = 0

            # Solved
            if row == 9:
                return True

            # Skip filled cells
            if board[row][col] != ".":
                return _helper(row, col + 1)

            for num in map(str, range(1, 10)):

                if is_valid(row, col, num):

                    board[row][col] = num

                    if _helper(row, col + 1):
                        return True

                    # Backtrack
                    board[row][col] = "."

            return False

        _helper(0, 0)