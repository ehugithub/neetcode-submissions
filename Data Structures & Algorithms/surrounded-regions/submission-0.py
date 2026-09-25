class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        seen = set()
        def onBorder(x, y):
            return x == 0 or x == m - 1 or y == 0 or y == n - 1

        def dfs(x, y):
            seen.add((x, y))
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] == 'O' and (new_x, new_y) not in seen:
                    dfs(new_x, new_y)

        for i in range(m):
            for j in range(n):
                if onBorder(i, j) and board[i][j] == 'O' and (i, j) not in seen:
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in seen:
                    board[i][j] = 'X'