from copy import deepcopy


def n_queens(matrix: list[list[int | str]], no_of_queens: int):

    n = len(matrix)

    def mark_attacks(board, row, col):

        # Mark row
        for j in range(n):
            if board[row][j] == 0:
                board[row][j] = 1

        # Mark column
        for i in range(n):
            if board[i][col] == 0:
                board[i][col] = 1

        # Mark left diagonal
        i, j = row, col
        while i < n and j >= 0:
            if board[i][j] == 0:
                board[i][j] = 1
            i += 1
            j -= 1

        # Mark right diagonal
        i, j = row, col
        while i < n and j < n:
            if board[i][j] == 0:
                board[i][j] = 1
            i += 1
            j += 1

    def _helper(board, queens_left, current_row):

        # Base Case
        if queens_left == 0:
            for row in board:
                print(row)
            print()
            return True

        # Out of rows
        if current_row >= n:
            return False

        found = False

        for col in range(n):

            # Safe position
            if board[current_row][col] == 0:

                # Create new board state
                new_board = deepcopy(board)

                # Place Queen
                new_board[current_row][col] = f"Q{current_row}"

                # Mark attacks
                mark_attacks(new_board, current_row, col)

                # Restore queen symbol
                new_board[current_row][col] = f"Q{current_row}"

                res = _helper(
                    new_board,
                    queens_left - 1,
                    current_row + 1
                )

                if res:
                    found = True

        return found

    return _helper(matrix, no_of_queens, 0)


matrix = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

print(n_queens(matrix, len(matrix)))