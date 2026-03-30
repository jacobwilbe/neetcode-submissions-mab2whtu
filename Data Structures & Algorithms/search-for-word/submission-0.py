class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(i, r, c):
            if i >= len(word):
                return True
            
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[i]:
                return False
            board[r][c] = "#"
            ret = False
            for x, y in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                dr = r + x
                dc = c + y
                if dfs(i + 1, dr, dc):
                    ret = True
            board[r][c] = word[i]
            return ret
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c):
                    return True
        return False

