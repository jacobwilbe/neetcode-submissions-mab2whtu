class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1,0), (0, 1), (-1, 0), (0, -1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        def bfs(row, col):
            visited = set()
            q = deque([(row, col, 0)])
            visited.add((row,col))
            while q:
                r, c, distance = q.popleft()
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    location = (new_r, new_c)
                    if new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS or location in visited or grid[new_r][new_c] == -1:
                        continue
                    if grid[new_r][new_c] > 0:
                        q.append((new_r, new_c, distance + 1))
                        visited.add(location)
                    elif grid[new_r][new_c] == 0:
                        grid[row][col] = distance + 1
                        return
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2147483647:
                    bfs(r,c)