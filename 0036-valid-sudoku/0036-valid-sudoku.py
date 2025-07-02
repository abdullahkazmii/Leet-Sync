class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        grids = [{} for _ in range(9)] 

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue

                grid_index = (r // 3) * 3 + (c // 3)

                rows[r][num] = rows[r].get(num, 0) + 1
                if rows[r][num] > 1:
                    return False

                cols[c][num] = cols[c].get(num, 0) + 1
                if cols[c][num] > 1:
                    return False

                grids[grid_index][num] = grids[grid_index].get(num, 0) + 1
                if grids[grid_index][num] > 1:
                    return False
        return True