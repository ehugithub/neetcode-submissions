class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        time = 0
        m = len(grid)
        n = len(grid[0])
        rotton = deque()
        num_fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotton.append((i, j))
                elif grid[i][j] == 1:
                    num_fresh += 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def spread(x, y):
            nonlocal num_fresh
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                    grid[new_x][new_y] = 2
                    num_fresh -= 1
                    rotton.append((new_x, new_y))
        
        while rotton and num_fresh > 0:
            layer = len(rotton)
            for _ in range(layer):
                r_x, r_y = rotton.popleft()
                spread(r_x, r_y)
            time += 1
        
        return -1 if num_fresh > 0 else time
        