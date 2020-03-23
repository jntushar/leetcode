"""

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.
The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

"""


"""---SOLUTION---"""

class Solution:
    def matrixReshape(self, nums, r, c):

        m = [[0] * c for _ in range(r)]
        rows, cols = 0, 0

        if r * c != len(nums) * len(nums[0]):
            return nums

        for i in range(len(nums)):
            for j in range(len(nums[0])):
                m[rows][cols] = nums[i][j]
                cols += 1
                if cols == c:
                    rows += 1
                    cols = 0
        return m