"""

Given two arrays, write a function to compute their intersection.

"""

"""---SOLUTION---"""

class Solution:
    def intersection(self, nums1, nums2):
        return set(nums1).intersection(set(nums2))