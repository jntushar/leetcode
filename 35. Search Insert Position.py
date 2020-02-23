"""

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

"""


"""---SOLUTION---"""


class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            index = 0
            for i in nums:
                if i < target:
                    index += 1
            return index
