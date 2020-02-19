"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

"""---SOLUTION---"""

class Solution:
    def twoSum(self, list1, target):
        """
        :type list1: List[int]
        :type target: int
        :rtype: List[int]
        """
        check = {}
        for i, y in enumerate(list1):
            x = target - y
            if x not in check:
                check[y] = i
            else:
                return [check[x], i]