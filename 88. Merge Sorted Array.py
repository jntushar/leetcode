"""

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:

    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

"""


"""---SOLUTION---"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m+n] = nums2
        nums1.sort()