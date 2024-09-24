public class Solution:
    def MaxValue(self, nums, k):
        n = len(nums)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            or_val = 0
            for j in range(min(i, k), 0, -1):
                or_val |= nums[i - 1]
                dp[i][j] = max(dp[i][j], dp[i - j][i - j] ^ or_val)
                for l in range(1, j):
                    dp[i][j] = max(dp[i][j], dp[i - l][i - l] ^ (or_val | nums[i - l - 1]))
        
        return dp[n][k]
