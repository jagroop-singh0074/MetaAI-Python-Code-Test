class Solution(object):
    def findLexSmallestString(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n, m = len(word1), len(word2)
        dp = [[] for _ in range(m)]
        dp[0].append(0)
        
        for i in range(m):
            for j in range(n):
                if word1[j] == word2[i]:
                    if i > 0 and dp[i-1] and j > dp[i-1][-1]:
                        dp[i].append(j)
                    elif i == 0:
                        dp[i].append(j)
        
        if not dp[-1]:
            return []
        
        res = dp[-1]
        for i in range(m):
            for j in dp[i]:
                if j < res[i]:
                    res[i] = j
        
        return res
