"""

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

"""


"""---SOLUTION---"""

class Solution:
    def singleNumber(self, nums):
        res = []

        for i in nums:
            if nums.count(i) < 2:
                res.append(i)
        return res