class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        grids = [{} for _ in range(9)] 

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                grid_index = (r // 3) * 3 + (c // 3)

                rows[r][board[r][c]] = rows[r].get(board[r][c], 0) + 1
                if rows[r][board[r][c]] > 1:
                    return False

                cols[c][board[r][c]] = cols[c].get(board[r][c], 0) + 1
                if cols[c][board[r][c]] > 1:
                    return False

                grids[grid_index][board[r][c]] = grids[grid_index].get(board[r][c], 0) + 1
                if grids[grid_index][board[r][c]] > 1:
                    return False
        return True