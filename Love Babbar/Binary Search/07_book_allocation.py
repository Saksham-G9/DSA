def book_allocation(books: list[int], m: int):
    #  [10,20,30,40], 2
    def _isPossibleSol(books: list[int], m: int, ans: int) -> bool:
        temp = m
        curr_sum = 0
        i = 0
        while temp:
            if i >= len(books):
                return False
            if curr_sum + books[i] > ans and curr_sum != 0:
                curr_sum = 0
                temp -= 1
            else:
                curr_sum += books[i]
                i += 1

        if i <= len(books) - 1:
            return False
        else:
            return True

    start, end = 0, sum(books)
    ans = -1
    while start <= end:
        mid = (start + end) // 2

        if _isPossibleSol(books, m, mid):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans


books = [10, 20, 30, 40, 50]
m = 2

print(book_allocation(books, m))
