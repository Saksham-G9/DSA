def prime_factorization(n: int) -> list[int]:
    ans = []

    i = 2

    while i * i <= n:
        while n % i == 0:
            ans.append(i)
            n //= i
        i += 1
    if n > 1:
        ans.append(n)
    return ans


print(prime_factorization(15))
