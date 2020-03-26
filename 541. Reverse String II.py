"""

Given a string and an integer k, you need to reverse the first k characters for every 2k characters
counting from the start of the string. If there are less than k characters left, reverse all of them.
If there are less than 2k but greater than or equal to k characters, then reverse the first k characters
and left the other as original.

"""

"""---SOLUTION---"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ""
        position = 0
        while position < len(s):
            strr = s[position: position + k]
            res = res + strr[::-1] + s[position + k: position + 2 * k]
            position += 2 * k
        return res

