class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        Build a 2D dp table that computes LCS that can be made
        up to those two letters
        '''
        ROWS = len(text1)
        COLS = len(text2)
        dp = [[0] * COLS for _ in range(ROWS)]
        dp[0][0] = 1 if text1[0] == text2[0] else 0

        # Fill first row
        for col in range(1, COLS):
            dp[0][col] = 1 if text1[0] == text2[col] else max(dp[0][col - 1], 0)
        
        # Fill first col, break if found match beecause no more can be made
        for row in range(1, ROWS):
            dp[row][0] = 1 if text2[0] == text1[row] else max(dp[row - 1][0], 0)

        for i in range(1, ROWS):
            for j in range(1, COLS):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[-1][-1]