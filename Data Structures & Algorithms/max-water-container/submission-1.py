class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        Start with pointers at opposite ends
        Calculate area and maximize result
        Move the pointer that is of lesser height
        '''
        res = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res
