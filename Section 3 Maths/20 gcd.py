import math
import sympy
a, b = 100, 24
res = 1
for i in range(min(a, b) + 1, 2, -1):
    if a % i == 0 and b % i == 0:
        res = i
        break

print(res)
print(math.gcd(a, b))
print(math.lcm(a,b))
print(sympy.isprime(23))