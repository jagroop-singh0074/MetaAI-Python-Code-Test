class Solution(object):
    def MaximizeSquareArea(self, m, n, hFences, vFences):
        MOD = 10**9 + 7
        hFences.sort()
        vFences.sort()
        
        max_h = self.getMaxGap(hFences, m)
        max_v = self.getMaxGap(vFences, n)
        
        res = -1
        for side in range(min(max_h, max_v), 0, -1):
            if self.canFormSquare(hFences, vFences, side):
                res = side * side % MOD
                break
        
        return res
    
    def getMaxGap(self, fences, length):
        max_gap = 0
        prev_fence = 1
        for fence in fences:
            max_gap = max(max_gap, fence - prev_fence)
            prev_fence = fence
        max_gap = max(max_gap, length - prev_fence)
        return max_gap
    
    def canFormSquare(self, hFences, vFences, side):
        hGaps = []
        vGaps = []
        
        prev_h = 1
        for fence in hFences:
            if fence - prev_h >= side:
                hGaps.append((prev_h, fence))
            prev_h = fence
        
        hGaps.append((prev_h, hFences[-1] + side))
        
        prev_v = 1
        for fence in vFences:
            if fence - prev_v >= side:
                vGaps.append((prev_v, fence))
            prev_v = fence
        
        vGaps.append((prev_v, vFences[-1] + side))
        
        for hGap in hGaps:
            for vGap in vGaps:
                if hGap[1] - hGap[0] >= side and vGap[1] - vGap[0] >= side:
                    return True
        
        return False
