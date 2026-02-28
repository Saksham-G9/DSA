def sum_of_digits(num: int):
    def helper(num: int):
        if num // 10 == 0:
            return num
        temp = num % 10
        return temp + helper(num // 10)

    return helper(abs(num))


print(sum_of_digits(-1111))
3