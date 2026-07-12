class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        # Perform House Robber I twice:
        # Once without first element
        # Another without last element

        def house_robber(houses):
            prev2 = 0
            prev1 = 0

            for h in houses:
                most = max(prev2 + h, prev1)
                prev2 = prev1
                prev1 = most

            return prev1

        return max(house_robber(nums[1:]), house_robber(nums[:-1]))