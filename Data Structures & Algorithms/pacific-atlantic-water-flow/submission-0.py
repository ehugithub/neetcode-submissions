class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        res = []
        n = len(heights[0]) # x axis (cols)
        m = len(heights) # y axis (rows)

        pacific = set([(0, y) for y in range(n)] + [(x, 0) for x in range(m)])
        atlantic = set([(m - 1, y) for y in range(n)] + [(x, n - 1) for x in range(m)])
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        q = deque(pacific)
        while q:
            x, y = q.popleft()
            pacific.add((x,y))

            for dx, dy in directions:
                n_x, n_y = x + dx, y + dy
                if 0 <= n_x < m and 0 <= n_y < n and (n_x, n_y) not in pacific and heights[n_x][n_y] >= heights[x][y]:
                    q.append((n_x, n_y))
        
        p = deque(atlantic)

        while p:
            x, y = p.popleft()
            atlantic.add((x,y))

            for dx, dy in directions:
                n_x, n_y = x + dx, y + dy
                if 0 <= n_x < m and 0 <= n_y < n and (n_x, n_y) not in atlantic and heights[n_x][n_y] >= heights[x][y]:
                    p.append((n_x, n_y))
        
        return [list(cd) for cd in pacific & atlantic]
        