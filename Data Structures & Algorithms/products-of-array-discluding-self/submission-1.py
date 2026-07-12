class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = [1] * len(nums)
        right_products = [1] * len(nums)

        # create left_products
        for i in range(1, len(nums)):
            left_products[i] = left_products[i - 1] * nums[i - 1]
        
        # create right_products
        for i in range(len(nums) - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]
        
        res = []
        for i in range(len(nums)):
            res.append(left_products[i] * right_products[i])

        return res