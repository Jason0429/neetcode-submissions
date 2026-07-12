class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        dp[amount + 1]
        dp[i] = minimum number of coins to to sum to `i`
        '''

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 # it takes 0 coins to sum to 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    # min of don't use this coin, or use this coin
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        return dp[-1] if dp[-1] != amount + 1 else -1

