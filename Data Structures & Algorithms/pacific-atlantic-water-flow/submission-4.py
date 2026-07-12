class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        DFS from each pacific cell to find all cells that can reach pacific
        DFS from each atlantic cell to find all cells that can reach atlantic
        Return union of pacific and atlantic coordinates
        '''

        res = []
        pacific = set()
        atlantic = set()
        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(r, c, ocean, from_height):
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or (r, c) in ocean
                # we are not tracking which cells can be reached from the ocean cells
                # we are tracking which cells can reach the ocean, naively
                or heights[r][c] < from_height
            ):
                return

            ocean.add((r, c))
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])

        return res