class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # left pointer start at the beginning
        # right pointer start at the end
        # if left + right > target, move right pointer down one
        # if left + right < target, move left pointer up one
        # else return the answer

        l = 0
        r = len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                # l should always be less than r
                # (1-indexed) value
                return [l + 1, r + 1]

        return [-1, -1]