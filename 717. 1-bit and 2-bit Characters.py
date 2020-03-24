"""

We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).
Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

"""


"""---SOLUTION---"""

class Solution:
    def isOneBitCharacter(self, bits):

        # oneBit = 0
        # twoBit = 10 or 11

        i = 0
        while i < len(bits):
            if (bits[i] == 1 and bits[i + 1] == 1) or (bits[i] == 1 and bits[i + 1] == 0):
                i += 2
                j = 1
            else:
                i += 1
                j = 0

        if j == 1:
            return False
        else:
            return True
