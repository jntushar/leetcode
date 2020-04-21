"""

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

"""

"""---SOLUTION---"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):

        visited = {}
        for index, num in enumerate(nums):
            if num in visited and index - visited[num] <= k:
                return True
            visited[num] = index
        return False