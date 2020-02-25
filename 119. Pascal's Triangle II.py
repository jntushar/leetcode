"""

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.

"""


"""---SOLUTION---"""


class Solution:
    def getRow(self, rowIndex):

        num = rowIndex + 1
        pascalTriangle = list([1] * n for n in range(1, num + 1))
        for i in range(2, num):
            for j in range(1, len(pascalTriangle[i]) - 1):
                pascalTriangle[i][j] = pascalTriangle[i - 1][j - 1] + pascalTriangle[i - 1][j]

        return pascalTriangle[rowIndex]
