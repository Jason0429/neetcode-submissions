class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Keep a left and right pointer
        Only move left if right is less than left
        Maximize the profit along the way
        '''

        l = 0
        res = 0

        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            res = max(res, profit)

            if prices[r] < prices[l]:
                l = r
        
        return res
            