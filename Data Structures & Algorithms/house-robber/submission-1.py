class Solution:
    def rob(self, nums: List[int]) -> int:
        # Solution 1
        # if len(nums) <= 2:
        #     return max(nums)
        
        # # dp[i] is the max money robbed up to house i
        # dp = list(nums)
        # dp[1] = max(nums[0], nums[1])
        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        # return dp[-1]

        # Solution 2
        prev2 = 0
        prev1 = 0

        for n in nums:
            most = max(n + prev2, prev1)
            prev2 = prev1
            prev1 = most
        
        return prev1
