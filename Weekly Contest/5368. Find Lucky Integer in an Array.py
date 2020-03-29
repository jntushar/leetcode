"""

Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.

"""


"""---SOLUTION---"""


class Solution:
    def findLucky(self, arr):
        res = []

        for i in arr:
            if i in res:
                continue
            if arr.count(i) == i:
                res.append(i)

        if len(res) == 0:
            return -1
        else:
            return max(res)
