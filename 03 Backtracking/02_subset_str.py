def printSubset(s: str, res: str):

    if len(s) == 0:
        print(res, end=", ")
        return

    printSubset(s[1:], res)
    printSubset(s[1:], res + s[0])


printSubset("abc", "")
