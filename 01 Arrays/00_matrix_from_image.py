def get_matrix():
    return [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50],
    ]


if __name__ == "__main__":
    mat = get_matrix()
    for row in mat:
        print(row)
