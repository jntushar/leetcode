"""

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

"""

"""---SOLUTION---"""

class Solution:
    def majorityElement(self, nums):
        visited = []
        count = {}
        for i in nums:
            if i not in visited:
                visited.append(i)
                count[i] = 1
            else:
                count[i] += 1
        return list(count.keys())[list(count.values()).index(max(count.values()))]
