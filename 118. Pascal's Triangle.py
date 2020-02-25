"""

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

"""


"""---SOLUTION---"""


class Solution:
    def generate(self, numRows):

        pascalTriangle = list([1] * n for n in range(1, numRows + 1))
        for i in range(2, numRows):
            for j in range(1, len(pascalTriangle[i]) - 1):
                pascalTriangle[i][j] = pascalTriangle[i - 1][j - 1] + pascalTriangle[i - 1][j]

        return pascalTriangle

