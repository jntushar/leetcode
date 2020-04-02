"""

Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

"""

""""---SOLUTION---"""


class Solution:
    def isHappy(self, n: int) -> bool:

        for _ in range(100):
            check = 0
            while n > 0:
                check += (n % 10) ** 2
                n = n // 10
            if check == 1:
                return True
                break
            else:
                n = check
