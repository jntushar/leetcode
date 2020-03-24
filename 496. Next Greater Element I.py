"""

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

"""

"""---SOLUTION---"""


class Solution:
    def nextGreaterElement(self, nums1, nums2):

        res = [-1] * len(nums1)

        for index, num in enumerate(nums1):
            i = nums2.index(num)
            for j in nums2[i:]:
                if j > num:
                    res[index] = j
                    break

        return res





