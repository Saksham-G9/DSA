def book_allocation(books: list[int], m: int):
    if m > len(books):
        return -1

    def can_allocate(books, m, max_pages):
        required = 1
        curr_sum = 0

        for pages in books:
            if curr_sum + pages > max_pages:
                required += 1
                curr_sum = pages
            else:
                curr_sum += pages

        return required <= m

    start, end = max(books), sum(books)
    ans = -1

    while start <= end:
        mid = (start + end) // 2

        if can_allocate(books, m, mid):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1

    return ans


books = [10, 20, 30, 40, 50]
m = 2

print(book_allocation(books, m))