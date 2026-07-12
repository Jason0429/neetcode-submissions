class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        Create dp of size amount + 1
        dp[i] is the number of ways to make `i`
        There is only 1 way to make 0
        Return dp[-1]
        '''

        dp = [0] * (amount + 1)
        dp[0] = 1

        # going by coin on the outer loop guarantees we will not reuse coins
        # therefore not creating duplicate combinations
        for c in coins:
            for a in range(1, amount + 1):
                if a - c >= 0:
                    dp[a] += dp[a - c]

        return dp[-1]