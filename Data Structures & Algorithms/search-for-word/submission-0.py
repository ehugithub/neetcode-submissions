class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        # we need to start at word[0], then search from there
        # keep track of used letters
        used = set()

        def backtrack(x, y, ind):
            if board[x][y] != word[ind]:
                return False
            if ind == len(word) - 1:
                return True

            used.add((x, y))
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                if (0 <= new_x < len(board) and
                   0 <= new_y < len(board[0]) and
                   (new_x, new_y) not in used):
                   if backtrack(new_x, new_y, ind + 1): return True
                
            used.remove((x, y))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0):
                        return True

        return False
        