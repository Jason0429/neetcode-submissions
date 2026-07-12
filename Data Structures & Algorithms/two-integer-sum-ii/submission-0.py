class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Two pointers
        current_sum = numbers[l] + numbers[r]
        if current_sum == target:
            return
        Move left pointer if current_sum < target
        Move right pointer if current_sum > target
        '''
        l = 0
        r = len(numbers) - 1

        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1

        return [l+1, r+1]

            



