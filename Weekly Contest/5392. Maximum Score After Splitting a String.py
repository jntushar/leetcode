"""

Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings
(i.e. left substring and right substring).
The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

"""


"""---SOLUTION---"""

from collections import Counter

class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        score = 0
        for i in range(1, n):
            a = Counter(s[:i])['0'] + Counter(s[i:])['1']
            score = max(score, a)
        return score