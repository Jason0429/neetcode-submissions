class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        If ROWS < 3 or COLS < 3, return because no O can be surrounded by Xs
        Go through board
        If O, bfs to find entire island of Os
        Check if that island is surrounded by Xs
        If so, change island to Xs
        '''
        X = 'X'
        O = 'O'
        ROWS = len(board)
        COLS = len(board[0])

        if ROWS < 3 or COLS < 3:
            return

        # an O along the edge of the board invalidates an island of Os from being surrounded by Xs
        def invalidates_island(r, c):
            return board[r][c] == O and (r == 0 or r == ROWS-1 or c == 0 or c == COLS-1)

        def is_candidate(r, c, visited):
            return board[r][c] == O and (r, c) not in visited

        def get_neighbors(r, c):
            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            neighbors = []

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    neighbors.append((nr, nc))
            
            return neighbors
        
        visited = set()
        def bfs(i, j):
            q = [(i, j)]
            island = []
            valid_island = True

            while q:
                r, c = q.pop(0)
                island.append((r, c))
                visited.add((r, c))

                if invalidates_island(r, c):
                    valid_island = False

                for nr, nc in get_neighbors(r, c):
                    if is_candidate(nr, nc, visited):
                        q.append((nr, nc))
            
            if valid_island:
                for r, c in island:
                    board[r][c] = X

        for i in range(1, ROWS-1):
            for j in range(1, COLS-1):
                if board[i][j] == O and (i, j) not in visited:
                    bfs(i, j)
