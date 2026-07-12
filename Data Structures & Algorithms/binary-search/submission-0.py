class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Initialize left and right to start and end of array
        Get mid point
        Check if mid element == target
        If target < mid element, move right to mid-1
        Otherwise, move left to mid+1
        If left > right, cancel and return -1
        '''

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            
            if nums[m] == target:
                return m
            
            if target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        
        return -1