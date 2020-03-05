"""

Given a non-empty array of integers, return the third maximum number in this array.
If it does not exist, return the maximum number. The time complexity must be in O(n).

"""

"""---SOLUTION---"""

class Solution:
    def thirdMax(self, nums):
        flag = 0
        firstMax = nums.pop(nums.index(max(nums)))
        x = firstMax
        for _ in range(len(nums)):
            maximum = nums.pop(nums.index(max(nums)))
            if maximum < x:
                flag += 1
            x = maximum
            if flag == 2:
                break

        if flag == 2:
            return maximum
        else:
            return firstMax

