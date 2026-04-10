def sqrt(n: int) -> int:
    start, end = 0, n // 2
    ans = -1

    while start <= end:
        mid = (start + end) // 2
        if mid * mid == n:
            return mid
        
        elif mid * mid < n:
            ans = mid
            start = mid + 1

        else:
            end = mid - 1

    return ans
 

print(sqrt(4))
print(sqrt(8))
print(sqrt(16))
print(sqrt(32))
