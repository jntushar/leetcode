"""

Given two positive integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.
Return a list of all powerful integers that have value less than or equal to bound.
You may return the answer in any order.  In your answer, each value should occur at most once.

"""

"""---SOLUTION---"""


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans = []
        for i in range(20):
            for j in range(20):
                num = x**i + y**j
                if num<=bound:
                    ans.append(num)
                else:
                    break
        return list(set(ans))