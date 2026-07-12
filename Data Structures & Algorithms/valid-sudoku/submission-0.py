class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        Create 3 collections of sets: columns, rows, sub-boxes
        Add each number visited to corresponding collection, return False if repeated
        '''
        def get_subbox_idx(i, j):
            return (j // 3) + 3 * (i // 3)


        BLANK = '.'

        # Left to right
        column_sets = [set() for _ in range(9)]

        # Top to bottom
        row_sets = [set() for _ in range(9)]

        # Top-left to Bottom-right
        subbox_sets = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                item = board[i][j]

                if item == BLANK:
                    continue
                if item in row_sets[i]:
                    return False
                if item in column_sets[j]:
                    return False

                subbox_idx = get_subbox_idx(i, j)
                if item in subbox_sets[subbox_idx]:
                    return False
                
                row_sets[i].add(item)
                column_sets[j].add(item)
                subbox_sets[subbox_idx].add(item)
        
        return True

                


