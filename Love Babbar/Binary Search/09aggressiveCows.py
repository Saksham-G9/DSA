def aggressiveCows(stalls, k):
    def _is_possible(stalls: list[int], k: int, ans: int):
        curr_k = 1
        lastPos = 0

        for i in range(1, len(stalls)):
            if stalls[i] - stalls[lastPos] >= ans:
                curr_k += 1
                lastPos = i
                if curr_k >= k:
                    return True

        return False

        
    # Write your code here.
    stalls.sort()
    start, end = 0, max(stalls) - min(stalls)

    ans = -1

    while start <= end:
        mid = (start + end) // 2

        if _is_possible(stalls, k, mid):
            ans = mid
            start = mid + 1
        else:
            end = mid - 1

    return ans