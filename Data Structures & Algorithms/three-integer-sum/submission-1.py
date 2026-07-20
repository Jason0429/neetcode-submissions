class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force (O(n^3)) to check every combination that adds to 0.
        # sort the numbers in increasing order to apply pointers for faster solution.
        # Outer loop O(n), up to length - 2 (to account for l, r pointers)
        # two pointers in an inner loop O(n)
        # check outer loop pointer + left pointer + right pointer adds to 0.
        # skip duplicate outer, left, and right to avoid duplicate triplets
        # if sum > 0, move right pointer down
        # if sum < 0, move left pointer up
        # inner loop ends when l >= r (must all be distinct)
        # store all possible combinations in a list
        # time complex: O(n^2)
        # space complex: O(n)

        answers = list()
        sorted_nums = sorted(nums)
        length = len(sorted_nums)

        for i in range(length - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue # skip duplicate anchors

            l = i + 1
            r = length - 1

            while l < r:
                total = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]
                if total == 0:
                    answers.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1
                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1 # skip duplicate lefts
                    while l < r and sorted_nums[r] == sorted_nums[r + 1]:
                        r -= 1 # skip duplicate rights
                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return answers