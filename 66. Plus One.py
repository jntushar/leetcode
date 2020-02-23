"""

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

"""

"""---SOLUTION---"""


class Solution:
    def plusOne(self, digits):
        x = 0

        for i in digits:
            x = x * 10 + i

        x = x + 1
        x = str(x)
        length = len(x)
        dig = [0] * length
        for i in range(length):
            dig[i] = int(x[i])
        return dig
