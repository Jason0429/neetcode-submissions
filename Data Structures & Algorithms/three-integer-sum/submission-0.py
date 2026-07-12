class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Sort `nums` first so that it makes it easier to not reuse duplicate values and
        makes finding 2nd and 3rd values exactly like "Two Sum II" with two pointers

        Use one loop for 1st value
        Stop loop if reaches positive value (cannot possibly be first value in triplet)
        Skip over if value same as last (duplicate)

        Use two pointers, l = i+1, r = len(nums) - 1 and
        perform "Two Sum II" to find values that add up to the remaining amount needed
        to sum to 0.
        If a + nums[l] + nums[r] == 0, it is possible that subsequent values of nums[l] + nums[r]
        also yield the required amount, so l += 1 and r -= 1

        Time: O(nlogn) + O(n^2)
        Space: O(n) sorting
        '''
        res = []

        nums.sort()

        for i, a in enumerate(nums):
            if a > 0: # reached positive value, cannot form triplet
                break
            
            if i > 0 and a == nums[i - 1]: # duplicate, skip
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = a + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r: # left is duplicate, skip
                        l += 1
        return res