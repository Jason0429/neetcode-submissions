class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        # as long as the profit is not negative, keep left idx
        # once it is negative, change l = r

        l = 0

        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
            else:
                max_profit = max(max_profit, profit)
        
        return max_profit

