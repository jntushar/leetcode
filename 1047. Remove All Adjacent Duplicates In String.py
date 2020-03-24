"""

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
We repeatedly make duplicate removals on S until we no longer can.
Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

"""

"""---SOLUTION---"""

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []

        for i in S:
            if len(stack) == 0 or i != stack[-1]:
                stack.append(i)
            else:
                stack.pop(-1)

        res = ''
        for i in stack:
            res += i
        return res