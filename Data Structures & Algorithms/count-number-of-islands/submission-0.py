class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def get_neighbors(r, c):
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            neighbors = []
            
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    neighbors.append((nr, nc))

            return neighbors

        def is_candidate(r, c):
            return grid[r][c] == '1'

        def bfs(i, j):
            q = [(i, j)]

            while q:
                r, c = q.pop(0)
                grid[r][c] = 0
                for nr, nc in get_neighbors(r, c):
                    if is_candidate(nr, nc):
                        q.append((nr, nc))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] == '1'):
                    bfs(i, j)
                    res += 1

        return res