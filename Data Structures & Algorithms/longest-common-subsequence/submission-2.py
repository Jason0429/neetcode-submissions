class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Approach without creating extra row/col

        M, N = len(text1), len(text2)
        dp = [[0] * N for _ in range(M)]

        # Check if first letters of each word match
        dp[0][0] = 1 if text1[0] == text2[0] else 0

        # Fill out first column, taking the max len along the way
        for i in range(1, M):
            dp[i][0] = max(dp[i-1][0], 1 if text1[i] == text2[0] else 0)
        
        # Fill out first row, taking the max len along the way
        for i in range(1, N):
            dp[0][i] = max(dp[0][i-1], 1 if text1[0] == text2[i] else 0)

        # Fill rest of DP table
        for i in range(1, M):
            for j in range(1, N):
                # If letters match, we want to add one to
                # dp[i-1][j-1] when both letters are not considered because
                # we do not want to count repeats
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max([dp[i][j-1], dp[i-1][j]])

        return dp[-1][-1]