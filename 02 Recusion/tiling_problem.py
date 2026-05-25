def tiling_problem(n: int) -> int:
    # Base Case
    if n == 0:
        return 1

    ans = 0
    if n >= 2:
        ans += tiling_problem(n - 2)

    ans += tiling_problem(n - 1)

    return ans

print(tiling_problem(4))