class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        WATER = -1
        TREASURE = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        '''
        Go through each item in grid
        If item is TREASURE, BFS from it and minimize distance to land cells
        '''

        def is_candidate(r, c):
            return grid[r][c] not in [WATER, TREASURE]

        def get_neighbors(r, c):
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            neighbors = []

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    neighbors.append((nr, nc))
            
            return neighbors

        def bfs(i, j):
            q = [] # should only hold land cells
            visited = set()

            for nr, nc in get_neighbors(i, j):
                if is_candidate(nr, nc):
                    q.append((nr, nc, 1))

            while q:
                r, c, distance = q.pop(0)
                visited.add((r, c))

                grid[r][c] = min(grid[r][c], distance)

                for nr, nc in get_neighbors(r, c):
                    if is_candidate(nr, nc) and (nr, nc) not in visited:
                        q.append((nr, nc, distance + 1))
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == TREASURE:
                    bfs(i, j)
