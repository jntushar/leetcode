"""

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.
If the last word does not exist, return 0.
Note: A word is defined as a maximal substring consisting of non-space characters only.

"""

"""---SOLUTION---"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()

        if len(s) >= 1:
            return len(s[-1])
        else:
            return 0