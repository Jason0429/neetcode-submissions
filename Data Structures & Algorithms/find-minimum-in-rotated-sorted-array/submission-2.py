class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        curr_min = float("inf")

        while l < r:
            m = l + (r - l) // 2
            curr_min = min(curr_min, nums[m])

            # min is on the right side
            if nums[m] > nums[r]:
                l = m + 1
            else: # min is on the left side
                r = m - 1

        # l == r at this point
        return min(curr_min, nums[l])