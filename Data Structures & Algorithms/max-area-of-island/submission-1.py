class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        Go through each cell
        If cell is 1, start bfs, keeping track of how big the island is
        Change island cells to 0 as you visit them
        Update max island
        '''

        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def is_candidate(coord, queue):
            r, c = coord
            return grid[r][c] == 1 and (r, c) not in queue

        def get_neighbors(r, c):
            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            neighbors = []

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    neighbors.append((nr, nc))

            return neighbors
        
        def bfs(i, j):
            q = [(i, j)]
            size = 0

            while q:
                r, c = q.pop(0)
                size += 1
                grid[r][c] = 0
                for nr, nc in get_neighbors(r, c):
                    if is_candidate((nr, nc), q):
                        q.append((nr, nc))
            
            return size

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    res = max(res, bfs(i, j))

        return res