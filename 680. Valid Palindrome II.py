"""

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

"""


"""---SOLUTION---"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        for index in range(len(s) - 1):
            if s[index] != s[-index - 1]:
                return s[index: -index - 2] == s[index + 1: -index - 1][::-1] or s[index + 1: -index - 1] == s[index + 2: len(s) - index][::-1]
        return False
