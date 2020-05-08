"""

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet,
return true if and only if the given words are sorted lexicographicaly in this alien language.

"""

"""---SOLUTION---"""


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        index = {}
        for i in range(len(order)):
            index[order[i]] = i

        for i in range(len(words) - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    if index[words[i][j]] > index[words[i + 1][j]]:
                        return False
                    break
            else:
                if len(words[i]) > len(words[i + 1]):
                    return False

        return True