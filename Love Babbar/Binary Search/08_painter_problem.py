def findLargestMinDistance(boards: list[int], k: int):
    def _is_possible(boards: list[int], k: int, ans: int):
        curr_k = 1
        curr_sum = 0

        for wall in boards:
            if wall > ans:
                return False
            if curr_sum + wall > ans:
                curr_k += 1
                curr_sum = wall
            else:
                curr_sum += wall

        return curr_k <= k

    start, end = max(boards), sum(boards)

    ans = -1

    while start <= end:
        mid = (start + end) // 2

        if _is_possible(boards, k, mid):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1

    return ans


boards = [5, 5, 5, 5]
k = 2

print(findLargestMinDistance(boards, k))
