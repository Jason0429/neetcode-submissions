class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Perform binary search
        If nums[l] < target < nums[m], r = m - 1
        else, l = m + 1
        If nums[m] == target: return m
        return -1
        '''

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            
            # what case would it be on the left half?
            if (nums[l] < nums[m] and nums[l] <= target < nums[m]) \
                or (nums[l] > nums[m] and nums[l] <= target) \
                or (nums[l] > nums[m] and target < nums[m]):
                r = m - 1
            else:
                l = m + 1
            
        return -1