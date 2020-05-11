"""

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...

"""

"""---SOLUTION---"""


class Solution:
    def convertToTitle(self, n: int) -> str:
        res = []
        ans = ''
        while n - 1 > 0:
            n, i = (n - 1) // 26, (n - 1) % 26
            res.append(i)

        if not n - 1:
            res.append(n - 1)

        for i in reversed(res):
            ans += chr(i + 65)
        return ans
