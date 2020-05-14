"""

Count the number of prime numbers less than a non-negative number, n.

Example:
    Input: 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

"""

"""---SOLUTION---"""

class Solution:
    def countPrimes(self, n: int) -> int:
        prime,ans=[True]*(n+1),0
        for i in range(2,n):
            if prime[i]:
                ans+=1
                temp=2*i
                while temp<=n:
                    prime[temp]=False
                    temp+=i
        return ans