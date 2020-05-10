"""

In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:
    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.

You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.
If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

"""

"""---SOLUTION---"""


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        hmap = {}
        for i in range(N):
            hmap[i + 1] = []

        for i in range(len(trust)):
            hmap[trust[i][0]].append(trust[i][1])

        judge = 0
        for key, value in hmap.items():
            if len(value) == 0:
                judge = key

        if judge == 0:
            return -1

        for key, value in hmap.items():
            if key == judge:
                continue
            if judge not in value:
                return -1
        return judge

