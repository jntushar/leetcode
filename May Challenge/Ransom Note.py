"""

Given an arbitrary ransom note string and another string containing letters from all the magazines,
write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

"""

"""---SOLUTION---"""

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magazine_counter = Counter(magazine)
        ransomNote_counter = Counter(ransomNote)

        for i in ransomNote_counter.keys():
            if ransomNote_counter[i] <= magazine_counter[i]:
                continue
            else:
                return False
        return True