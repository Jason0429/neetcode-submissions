class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = [1] * len(nums)
        right_products = [1] * len(nums)

        def get_left_product(p, i):
            if i == 0:
                return 1
            
            return p[i]


        def get_right_product(p, i):
            if i == len(nums) - 1:
                return 1
            
            return p[i]

        for i in range(1, len(left_products)):
            left_products[i] = nums[i-1] * get_left_product(left_products, i-1)
        
        for i in range(len(right_products) - 2, -1, -1):
            right_products[i] = nums[i+1] * get_right_product(right_products, i+1)

        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = left_products[i] * right_products[i]

        return res

