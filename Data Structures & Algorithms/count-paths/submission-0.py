class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        Build dp grid with size mxn
        Initialize the top row and left column to be 1s
        since there is only 1 way to get there from the starting point

        Starting at dp[1][1], dp[i][j] = sum of the top and left values
        resulting in the total way to get to that spot from the starting point

        Return the bottom right dp cell
        '''
        dp = [[0] * n for _ in range(m)]
        
        for c in range(n):
            dp[0][c] = 1
        
        for r in range(m):
            dp[r][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]