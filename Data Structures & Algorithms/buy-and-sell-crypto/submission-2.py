class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0

        for r in range(1, len(prices)):
            sell_price = prices[r]
            buy_price = prices[l]
            max_profit = max(max_profit, sell_price - buy_price)
            if sell_price < buy_price:
                l = r

        return max_profit