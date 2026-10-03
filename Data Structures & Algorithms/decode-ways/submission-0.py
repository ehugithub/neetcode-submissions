class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # num ways to decode s[0 : i]
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            # decode as a single char
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            
            # decode as double char
            if i > 1 and 10 <= int(s[i - 2] + s[i - 1]) <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
        