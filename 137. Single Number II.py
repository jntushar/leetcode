"""

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""

"""---SOLUTION---"""


class Solution:
    def singleNumber(self, nums):
        for i in nums:
            if nums.count(i) < 3:
                return i
