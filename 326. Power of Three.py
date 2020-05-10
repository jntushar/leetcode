"""

Given an integer, write a function to determine if it is a power of three.

"""

"""---SOLUTION---"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n>0:
            if n == 1:
                return True
            elif n%3==0:
                n=n/3
            else:
                return False
        return True