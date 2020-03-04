"""

A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.
Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

"""


"""---SOLUTION---"""


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = ""
        Count = 0
        s = 0

        for i in range(0, len(S)):
            if S[i] == '(':
                if Count == 0:
                    s = i + 1
                Count += 1
            elif S[i] == ')':
                Count -= 1
            if Count == 0:
                res += S[s:i]
                s = i + 1
        return res