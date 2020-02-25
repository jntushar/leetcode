"""

Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

"""


"""---SOLUTION---"""


class Solution:
    def maxProfit(self, prices):
        profit = 0
        minPrice = 99999999999
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] -minPrice > profit:
                profit = prices[i] - minPrice
        return profit