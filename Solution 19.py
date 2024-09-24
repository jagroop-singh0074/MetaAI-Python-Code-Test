class Solution:
    def maxValue(self, nums, k):
        n = len(nums)
        dp = [0] * (1 << n)
        for mask in range(1 << n):
            count = bin(mask).count('1')
            if count <= k:
                for i in range(n):
                    if mask & (1 << i):
                        dp[mask] |= nums[i]
        res = 0
        for mask in range(1 << n):
            if bin(mask).count('1') == k:
                res = max(res, dp[mask] ^ dp[(1 << n) - 1 - mask])
        return res
