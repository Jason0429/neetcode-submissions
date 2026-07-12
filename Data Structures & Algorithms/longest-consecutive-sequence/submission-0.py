class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # runs in O(n) because it does not surpass 2n actual iterations
        nums_set = set(nums)
        longest = 0

        for n in nums:
            # we want the START of a possible consecutive sequence
            if (n - 1) in nums_set:
                continue
            
            length = 1
            while (n + length) in nums_set:
                length += 1

            longest = max(length, longest)

        return longest