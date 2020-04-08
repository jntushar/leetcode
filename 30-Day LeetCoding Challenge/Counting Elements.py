"""

Given an integer array arr, count element x such that x + 1 is also in arr.
If there're duplicates in arr, count them seperately.

"""


"""---SOLUTION---"""

class Solution:
    def countElements(self, arr):

        res = 0
        for i in arr:
            if i + 1 in arr:
                res += 1
        return res