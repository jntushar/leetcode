"""

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

"""

"""---SOLUTION"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        length = len(s) - 1
        column = 0

        for i in range(len(s)):
            alphabet_number = ord(s[i])
            if alphabet_number > 90:
                alphabet_number -= 96
            else:
                alphabet_number -= 64
            column += alphabet_number * (26 ** length)
            length -= 1
        return column