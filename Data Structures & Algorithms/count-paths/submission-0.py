class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n] * m # m rows, n columns

        dp[0][0] = 1

        for i in range(0, m):
            for j in range(1, n):
                from_left = 0
                from_top = 0

                if i > 0:
                    from_top = dp[i - 1][j]
                if j > 0:
                    from_left = dp[i][j - 1]
                
                dp[i][j] = from_top + from_left

        print(dp)
        return dp[m - 1][n - 1]
        