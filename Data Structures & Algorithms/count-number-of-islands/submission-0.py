class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def valid(r, c):
            return 0 <= r < m and 0 <= c < n

        def dfs(i, j):
            grid[i][j] = "0"
            for dy, dx in directions:
                nr, nc = i + dy, j + dx
                
                if valid(nr, nc) and grid[nr][nc] == "1":
                    dfs(nr, nc)


        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)
        
        return ans