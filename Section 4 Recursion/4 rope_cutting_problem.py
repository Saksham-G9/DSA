def rope_cutting(n: int, a: int, b: int, c: int) -> int:
    max_pieces = -1

    def _helper(n: int, pieces=0):
        nonlocal max_pieces
        if n == 0:
            max_pieces = max(max_pieces, pieces)
            return
        if n < 0:
            return

        _helper(n - a, pieces + 1)
        _helper(n - b, pieces + 1)
        _helper(n - c, pieces + 1)

    _helper(n, 0)
    return max_pieces


print(rope_cutting(9, 2, 2, 2))
