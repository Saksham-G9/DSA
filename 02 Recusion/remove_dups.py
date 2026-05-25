def remove_dups(s: str) -> str:
    print(dict.fromkeys(s))
    return "".join(dict.fromkeys(s))

s = "appnnacollege"
print(remove_dups(s))