class Solution:
    def trap(self, height: List[int]) -> int:
        LEN = len(height)

        # for each slot i, get the max heights to the left and right of i
        left_max_heights = [0] * LEN
        right_max_heights = [0] * LEN

        for i in range(1, LEN):
            left_max_heights[i] = max(left_max_heights[i - 1], height[i - 1])
        
        for i in range(LEN - 2, -1, -1):
            right_max_heights[i] = max(right_max_heights[i + 1], height[i + 1])

        print(left_max_heights)
        print(right_max_heights)

        # if left_max_heights[i] > 0 and right_max_heights[i] > 0, then water can be filled here
        # add it to max_area_water
        max_area_water = 0
        
        for i in range(LEN):
            if left_max_heights[i] > 0 and right_max_heights[i] > 0:
                max_area_water += max(0, min(left_max_heights[i], right_max_heights[i]) - height[i])

        return max_area_water