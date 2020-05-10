"""

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Follow up: Could you solve it without loops/recursion?

"""

"""---SOLUTION---"""

class Solution:
	def isPowerOfFour(self, n: int) -> bool:
		if n<=0: return False
		return n&(n-1)==0 and (n-1)%3==0
