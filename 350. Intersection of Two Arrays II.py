"""

Given two arrays, write a function to compute their intersection.

"""

"""---SOLUTION---"""


class Solution:
    def intersect(self, nums1, nums2):

        res = []
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                res.append(i)
        return res