temp = x = 1333
rev = 0
while x:
    rev = rev * 10 + x % 10
    x //= 10

print(rev == temp)
