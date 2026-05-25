def find_permutation(s: str, ans: str):

    # Base Case
    if len(s) == 0:
        print(ans)
        return

    for i in range(len(s)):
        ch = s[i]

        # Remove only current character
        remaining = s[:i] + s[i+1:]

        find_permutation(remaining, ans + ch)


find_permutation("abc", "")