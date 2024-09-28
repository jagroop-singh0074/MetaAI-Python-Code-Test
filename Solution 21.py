class Solution(object):
    def getResults(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        obstacles = []
        results = []
        
        for query in queries:
            if query[0] == 1:
                # Add obstacle to the list
                obstacles.append(query[1])
                obstacles.sort()
            elif query[0] == 2:
                # Check if block can be placed
                x, sz = query[1], query[2]
                idx = self.binary_search(obstacles, x)
                results.append(idx == len(obstacles) or x - obstacles[idx-1] >= sz if idx > 0 else x >= sz)
        
        return results
    
    def binary_search(self, arr, target):
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left
