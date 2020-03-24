"""

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

"""


"""---SOLUTION 1---"""

class Solution:
    def missingNumber(self, nums):
        i = 0
        while nums:
            if i in nums:
                i += 1
            else:
                return i


"""---SOLUTION 2---"""

class Solution:
    def missingNumber(self, nums):
        return sum(range(len(nums)+1)) - sum(nums)
