def check_palindrome(n: int) -> bool:
    def helper(val: int, rev_num: int) -> bool:
        if val == 0:
            return n == rev_num
        return helper(val // 10, rev_num * 10 + val % 10)

    return helper(n, 0)


print(check_palindrome(101))
