class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # with a sorted array, we can remove duplicates in-place with slow and fast pointers
        # while slow == fast, increment fast
        # once they are different, increment slow and write the fast value in the slow index
        # return slow + 1 for number of unique numbers

        # 2, 2, 3, 4, 5, 5
        #          l     r
        # 2, 3, 4, 5

        slow = 0

        for fast in range(1, len(nums)):
            if nums[fast] == nums[slow]:
                continue
            
            slow += 1
            nums[slow] = nums[fast]
        
        return slow + 1
