"""

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

"""


"""---SOLUTION---"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = []
        t = []
        for i in S:
            if i == '#' and len(s) > 0:
                s.pop(-1)
            elif i != '#':
                s.append(i)

        for j in T:
            if j == '#' and len(t) > 0:
                t.pop(-1)
            elif j != '#':
                t.append(j)

        if s == t:
            return True
        else:
            return False
