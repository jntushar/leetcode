"""

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

"""


"""---SOLUTION---"""


class Solution:
    def maxProfit(self, prices):
        first, second = 9999999999, 9999999999
        profitA, profitB = 0, 0

        for price in prices:
            first = min(first, price)
            profitA = max(profitA, price - first)
            second = min(second, price - profitA)
            profitB = max(profitB, price - second)
        return profitB
    