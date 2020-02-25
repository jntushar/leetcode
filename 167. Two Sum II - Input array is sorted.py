"""

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
Note:
    Your returned answers (both index1 and index2) are not zero-based.
    You may assume that each input would have exactly one solution and you may not use the same element twice.

"""


"""---SOLUTION---"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        check = {}
        for i, y in enumerate(numbers):
            x = target - y
            if x not in check:
                check[y] = i
            else:
                return [check[x] + 1, i + 1]