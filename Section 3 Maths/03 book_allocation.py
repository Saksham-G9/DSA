def book_allocation(arr: list[int], k: int) -> int:
    if k > len(arr):
        return -1
    start, end = max(arr), sum(arr)

    low, high = start, end
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if isPossibleAns(mid, arr, k):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


def isPossibleAns(ans: int, arr: list[int], k: int):
    curr_sum = 0
    student_used = 1
    for el in arr:
        if el > ans:
            return False
        if curr_sum + el > ans:
            student_used += 1
            curr_sum = el
            if student_used > k:
                return False
        else:
            curr_sum += el
    return True


arr = [19, 9, 30, 22, 7]
k = 4

print(book_allocation(arr, k))
