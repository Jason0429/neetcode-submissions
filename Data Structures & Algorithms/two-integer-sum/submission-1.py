class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = dict() # value : index

        for i, n in enumerate(nums):
            if target - n in visited:
                return [visited[target - n], i]
            visited[n] = i