"""

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.

"""


"""---SOLUTION---"""


class Solution:
    def maxArea(self, height):
        capacity = 0
        left = 0
        right = len(height) - 1
        while left < right:
            capacity = max(capacity, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return capacity

