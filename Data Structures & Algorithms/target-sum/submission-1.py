class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        Try every possible combination with and cache results (index, number of ways)
        Add the number of ways you can reach target when adding and subtracting each value
        '''
        dp = dict() # (index, total number of ways)

        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0

            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
            return dp[(i, total)]

        return dfs(0, 0)