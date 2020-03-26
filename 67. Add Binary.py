"""

Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

"""


"""---SOLUTION---"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        integer_sum = int(a, 2) + int(b, 2)

        binary_sum = bin(integer_sum)

        return binary_sum[2:]