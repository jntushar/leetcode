"""

Given a positive integer num, write a function which returns True if num is a perfect square else False.


"""

"""---SOLUTION---"""
import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if str(math.sqrt(num))[-1] == '0':
            return True
        return False