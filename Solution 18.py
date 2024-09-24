class Solution(object):
    def maxScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        unique = set()
        dp = [0] * cols
        
        for row in grid:
            temp = dp[:]
            for j, val in enumerate(row):
                if val not in unique:
                    unique.add(val)
                    for k in range(cols):
                        if dp[k] > 0 or k == j:
                            temp[k] = max(temp[k], dp[k] + val)
            unique.clear()
            dp = temp
        
        return max(dp)
