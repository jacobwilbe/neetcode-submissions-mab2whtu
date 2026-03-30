class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #do bfs at treasure instead of INF, multi source BFS
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        visited = set()
        INF = 2147483647

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        while q:
            r, c = q.popleft()
            for dr, dc in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == -1:
                    continue
                if grid[nr][nc] != INF:
                    continue
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))
            
