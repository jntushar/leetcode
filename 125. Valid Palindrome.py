"""

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

"""

"""---SOLUTION 1---"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strr = ''
        for i in s:
            if (ord(i) >= 65 and ord(i)<=90) or (ord(i) >=97 and ord(i) <= 122) or (ord(i) >=48 and ord(i) <= 57):
                strr += i.lower()

        if strr == strr[::-1]:
            return True
        else: return False

"""---SOLUTION 2---"""

import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower().replace(" ","").translate(str.maketrans('', '', string.punctuation))
        return True if s[::-1]==s else False
