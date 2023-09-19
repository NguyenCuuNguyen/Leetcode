"""
121: 
:type prices: List[int]
:prices[i] is the price of a given stock on the ith day.
==> maximum profit
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Brute force: Space = O(1), Time Limit Exceeded: Time = O(N^2)
        """
        max_so_far = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1, n):
                max_so_far = max(max_so_far, prices[j] - prices[i])
        return max_so_far

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

    
    def maxProfit(self, prices: List[int]) -> int:
        """Kadane algorithm: if profit >0, keep adding differnces. Otherwise setback to 0
        Time: O(N), Space: O(1)
        """
        max_here, cur = 0,0 
        n = len(prices)
        for i in range(1, n):
            cur = max(cur + prices[i] - prices[i-1], 0)
            max_here = max(cur, max_here)
        return max_here


    def maxProfit(self, prices: List[int]) -> int:
        """Keep Min element throughout, subtract current with min and compare that with current max
        Time: O(N), Space: O(1)
        """
        max_here, min_here = 0, prices[0]
        n = len(prices)
        for i in range(1, n):
            min_here = min(prices[i], min_here)
            max_here = max(prices[i] - min_here, max_here)

        return max_here