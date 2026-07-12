class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Use binary search to narrow down to the row that it could be in
        Then binary search that row, return False if cannot be found
        '''

        top_row = 0
        bottom_row = len(matrix) - 1
        ROWS = len(matrix)
        COLS = len(matrix[0])

        if target < matrix[0][0] or target > matrix[ROWS-1][COLS-1]:
            return False

        while top_row <= bottom_row:
            mid_row = top_row + ((bottom_row - top_row) // 2)

            # is target in this row?
            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                l = 0
                r = COLS
                
                while l <= r:
                    m = l + ((r - l) // 2)

                    if matrix[mid_row][m] == target:
                        return True
                    
                    if target < matrix[mid_row][m]:
                        r = m - 1
                    else:
                        l = m + 1
            
            if target < matrix[mid_row][0]:
                bottom_row = mid_row - 1
            else:
                top_row = mid_row + 1
        
        return False