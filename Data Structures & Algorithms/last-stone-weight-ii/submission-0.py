class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = sum(stones)
        m, n = len(stones), s >> 1
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i, x in enumerate(stones, 1):
            for j in range(n + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= x:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - x] + x)
        return s - 2 * dp[-1][-1]
