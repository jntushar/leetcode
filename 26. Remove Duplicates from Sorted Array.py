"""

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

"""

"""---SOLUTION---"""


class Solution:
    def removeDuplicates(self, nums):
        if nums == []:
            return 0
        x = nums[0]
        for i in nums[1:]:
            if x == i:
                nums.remove(i)
            else:
                x = i
        return len(nums)






