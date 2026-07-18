class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Go through each number (n)
        # if (target - n) is seen already, we have both indicies, return answer.
        # We can keep track of seen with a dictionary.

        num_to_idx = dict()

        for idx, num in enumerate(nums):
            diff = target - num

            if diff in num_to_idx:
                if idx < num_to_idx[diff]:
                    return [idx, num_to_idx[diff]]
                else:
                    return [num_to_idx[diff], idx]

            num_to_idx[num] = idx