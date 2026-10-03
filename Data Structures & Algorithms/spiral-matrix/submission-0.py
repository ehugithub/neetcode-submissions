class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        bot = m - 1
        left = 0
        right = n - 1
        res = []

        while top <= bot and left <= right:
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1
            for row in range(top, bot + 1):
                res.append(matrix[row][right])
            right -= 1
            if top <= bot:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bot][col])
                bot -= 1
            if left <= right:
                for row in range(bot, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1
            
        return res
        