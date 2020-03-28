"""

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1. 

"""

"""---SOLUTION---"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
        return -1