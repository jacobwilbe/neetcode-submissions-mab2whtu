class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh = 0
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        minutes = 0
        if fresh == 0:
            return 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                        continue
                    if grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1
                    if fresh == 0:
                        return minutes + 1
            minutes += 1
        
        return -1


            