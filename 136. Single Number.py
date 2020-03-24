"""

Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""


"""---SOLUTION 1---"""

class Solution:
    def singleNumber(self, nums) -> int:
        for i in nums:
            if nums.count(i) < 2:
                return i


"""---SOLUTION 2---"""

class Solution:
    def singleNumber(self, nums) -> int:
        res = 0
        for num in nums:
            res^=num
        return res