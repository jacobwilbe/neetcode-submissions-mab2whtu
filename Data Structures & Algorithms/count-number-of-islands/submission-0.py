class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        total = 0
        rows, cols = len(grid), len(grid[0])
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                directions = [[-1, 0], [1, 0], [0, -1], [0,1]]
                row, col = q.popleft()
                for dr, dc in directions:
                    d_row, d_col = row + dr, col + dc
                    if (d_row in range(rows) and d_col in range(cols)) and ((d_row,d_col) not in visited) and (grid[d_row][d_col] == "1"):
                        visited.add((d_row,d_col))
                        q.append((d_row,d_col))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    total += 1
        return total