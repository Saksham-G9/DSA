class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        sum = 0
        len_mat = len(mat)
        for i, row in enumerate(mat):

            sum += row[i]
            if i != len_mat - 1 - i:
                sum += row[len_mat - 1 - i]
        return sum