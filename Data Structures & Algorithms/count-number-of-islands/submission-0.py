class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        # keep track of all nodes we already visited
        visited = set()
        m = len(grid)
        n = len(grid[0])

        def dfs(x, y):
            visited.add((x, y))
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == "1" and (new_x, new_y) not in visited:
                    dfs(new_x, new_y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    count += 1

        return count
        