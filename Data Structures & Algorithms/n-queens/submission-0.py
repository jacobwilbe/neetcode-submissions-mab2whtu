class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #our condition is basically checking if another queen lies on a row col or diagonal
        #check for rows by just checking 
        res = []
        board = [["."]*n for i in range(n)]
        col = set()
        posDiag = set()
        negDiag = set()
        def dfs(r):
            if r >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                diag = r + c
                n_diag = r - c
                if diag in posDiag or n_diag in negDiag or c in col:
                    continue
                board[r][c] = "Q"
                posDiag.add(diag)
                negDiag.add(n_diag)
                col.add(c)

                dfs(r+1)

                board[r][c] = "."
                posDiag.remove(diag)
                negDiag.remove(n_diag)
                col.remove(c)
        dfs(0)
        return res

                