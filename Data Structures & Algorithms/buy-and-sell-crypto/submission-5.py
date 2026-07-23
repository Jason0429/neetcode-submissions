class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_day = 0

        for sell_day in range(1, len(prices)):
            profit = prices[sell_day] - prices[buy_day]
            max_profit = max(max_profit, profit)

            if profit < 0:
                buy_day = sell_day

        return max_profit
            


