"""

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.


"""

"""---SOLUTION---"""


class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        ptr = 0

        for index, num in enumerate(nums):
            if num != 0:
                nums[ptr], nums[index] = nums[index], nums[ptr]
                ptr += 1

