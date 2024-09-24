class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        for _ in range(k):
            min_val = min(nums)
            min_idx = nums.index(min_val)
            nums[min_idx] = (min_val * multiplier) % MOD
        
        return [(val % MOD) for val in nums]
