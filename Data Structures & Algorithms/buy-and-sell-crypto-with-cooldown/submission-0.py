class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        State: Buy or Sell
        If Buy -> i + 1
        If Sell -> i + 2
        '''

        dp = dict() # (i, is_buying) : max_profit

        def dfs(i, is_buying):
            if i >= len(prices):
                return 0

            if (i, is_buying) in dp:
                return dp[(i, is_buying)]
            
            # cooldown is always an option
            cooldown = dfs(i + 1, is_buying)

            if is_buying:
                buy = dfs(i + 1, not is_buying) - prices[i]
                dp[(i, is_buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not is_buying) + prices[i]
                dp[(i, is_buying)] = max(sell, cooldown)
            
            return dp[(i, is_buying)]
        
        return dfs(0, True)

