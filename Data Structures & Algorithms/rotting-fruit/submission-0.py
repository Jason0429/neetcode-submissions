class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY = 0
        FRESH = 1
        ROTTEN = 2
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh_count = 0
        q = []

        '''
        Count how many fresh fruits there are initially
        Push rotten fruits into queue
        Perform bfs and keep track of iterations (seconds) it took
        If not all fresh fruits turn rotten, return -1
        Otherwise return the seconds it took
        '''

        def is_candidate(r, c):
            return grid[r][c] == FRESH
        
        def get_neighbors(r, c):
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            neighbors = []

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    neighbors.append((nr, nc))
            
            return neighbors

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == FRESH:
                    fresh_count += 1
                elif grid[i][j] == ROTTEN:
                    q.append((i, j))

        seconds = 0
        while fresh_count > 0 and q:
            q_len = len(q)
            for _ in range(q_len):
                r, c = q.pop(0)
                for nr, nc in get_neighbors(r, c):
                    if is_candidate(nr, nc):
                        grid[nr][nc] = ROTTEN
                        fresh_count -= 1
                        q.append((nr, nc))
                        
            seconds += 1

        return seconds if fresh_count == 0 else -1