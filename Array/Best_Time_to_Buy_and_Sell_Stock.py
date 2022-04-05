"""
121: 
:type prices: List[int]
:prices[i] is the price of a given stock on the ith day.
==> maximum profit
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        If the current price is less than the minimum value, store it as minimum
        Else Find the difference and max it with profit.        
        """
        if len(prices) < 2:
            return 0
        mn, profit = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < mn:
                mn = prices[i]
            else:
                profit = max(prices[i]-mn,profit)
        return profit
    