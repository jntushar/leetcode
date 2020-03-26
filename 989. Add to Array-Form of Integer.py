"""

For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].
Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

"""


"""---SOLUTION 1 ---"""

class Solution:
    def addToArrayForm(self, A, K):
        res = []

        num = 0
        for i in A:
            num = num * 10 + i

        num += K

        if num == 0:
            res.append(num)

        while num > 0:
            res.append(num % 10)
            num = num // 10

        return res[::-1]


"""---SOLUTION 2---"""

class Solution:
    def addToArrayForm(self, A, K):
        return(list(str(int((''.join([str(i) for i in A])))+K)))