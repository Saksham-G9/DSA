import math

x = 4000
res = 1
for i in range(1, x + 1):
    res *= i


def fact_rec(x: int) -> int:
    if x == 0 or x == 1:
        return 1

    return x * fact_rec(x - 1)

print(fact_rec(x))
print(res)
print(math.factorial(x))
