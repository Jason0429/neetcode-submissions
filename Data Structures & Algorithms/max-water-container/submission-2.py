class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force: calculate all possible areas and return the max (O(n^2))
        # optimal: left pointer at the start, right pointer at the end
        # calculate area, track maximum
        # move the pointer with the shorter height (this guarantees that we keep the outermost tallest,
        # which contributes to a greater area)
        # If heights are the same, move both
        # continue while left < right

        l = 0
        r = len(heights) - 1
        max_area = 0
        
        while l <= r:
            area = (r - l) * min(heights[l], heights[r])
            max_area = max(max_area, area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        
        return max_area

