class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        Find all the cells the starting pacific cells can flow to
        Find all the cells the starting atlantic cells can flow to
        Return the union of those two collections
        '''

        ROWS = len(heights)
        COLS = len(heights[0])
        pacific = set()
        atlantic = set()

        def get_neighbors(r, c):
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            neighbors = []

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    neighbors.append((nr, nc))

            return neighbors
        
        # heights[r][c] >= from_height because neighbor must be greater than or equal to itself for water to flow to it
        def is_candidate(r, c, from_height, visited):
            return heights[r][c] >= from_height and (r, c) not in visited

        def bfs(i, j, visited):
            q = [(i, j)]

            while q:
                r, c = q.pop(0)
                visited.add((r, c))

                for nr, nc in get_neighbors(r, c):
                    if is_candidate(nr, nc, heights[r][c], visited):
                        q.append((nr, nc))
        
        for c in range(COLS):
            bfs(0, c, pacific)
            bfs(ROWS-1, c, atlantic)
        
        for r in range(ROWS):
            bfs(r, 0, pacific)
            bfs(r, COLS-1, atlantic)
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res