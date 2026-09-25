class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        coins.sort()

        for i in range(amount + 1):
            for c in coins:
                if c > i:
                    break
                if dp[i - c] != sys.maxsize:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        
        return dp[amount] if dp[amount] != sys.maxsize else -1

        