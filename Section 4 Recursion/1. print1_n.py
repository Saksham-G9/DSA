def print_one_to_n(n: int) -> None:
    if n < 1:
        return

    print_one_to_n(n - 1)
    print(n, end=" ")


def print_n_to_one(n: int) -> None:
    if n < 1:
        return

    print(n, end=" ")
    print_n_to_one(n - 1)


print_n_to_one(10)
