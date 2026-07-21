class Solution:
    def trap(self, height: List[int]) -> int:
        # max left
        # 0 0 2 2 3 3 3 3 3 3
        
        # max right
        # 3 3 3 3 3 3 3 2 1 0

        # min(max_left, max(0, max_right - curr_height))
        # 0 0 2 0 2 3 2 0 0 0

        # return sum of that

        if len(height) == 0:
            return 0

        max_left = [0] * len(height)
        curr_max = height[0]

        for i in range(1, len(height)):
            max_left[i] = curr_max
            curr_max = max(curr_max, height[i])
        
        max_right = [0] * len(height)
        curr_max = height[-1]

        for i in range(len(height) - 2, -1, -1):
            max_right[i] = curr_max
            curr_max = max(curr_max, height[i])

        height_of_water = [0] * len(height)

        for i in range(len(height)):
            height_of_water[i] = max(0, min(max_left[i], max_right[i]) - height[i])
        
        return sum(height_of_water)


