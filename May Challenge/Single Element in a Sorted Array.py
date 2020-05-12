"""

You are given a sorted array consisting of only integers where every element appears exactly twice,
except for one element which appears exactly once. Find this single element that appears only once.

Example:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

"""

"""---SOLUTION---"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                return nums[i]

"""---BETTER SOLUTION---"""

# Using Binary Search

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = 2 * ((lo + hi) // 4)
            if nums[mid] == nums[mid+1]:
                lo = mid+2
            else:
                hi = mid
        return nums[lo]