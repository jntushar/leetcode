"""

Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""


"""---SOLUTION---"""

from math import inf

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        difference = inf

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == target:
                    return total

                elif total < target:
                    left += 1
                else:
                    right -= 1

                if abs(target - total) < difference:
                    difference = abs(target - total)
                    res = total
        return res