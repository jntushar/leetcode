"""

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

"""


"""---SOLUTION---"""


class Solution:
    def maxSubArray(self, nums):
        T=[0]*len(nums)
        T[0]=nums[0]
        for i in range(1,len(nums)):
            T[i]=max(T[i-1]+nums[i],nums[i])
        return max(T)
