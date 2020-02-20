"""

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

"""

"""---SOLUTION---"""


class Solution:
    def reverse(self, x):
        if x > 0:
            y = x
        else:
            y = -x
        num = 0
        while y > 0:
            a = y % 10
            num = num * 10 + a
            y = y // 10
        if num >= 2**31-1 or num <= -2**31: return 0
        if x > 0:
            return num
        else:
            return -num
