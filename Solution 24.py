class Solution(object):
    def maximumValueSum(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        m, n = len(board), len(board[0])
        max_sum = float('-inf')
        
        # Get max values for each row
        row_max = [max(row) for row in board]
        
        # Iterate over columns
        for i in range(n):
            for k in range(i, n):
                # Calculate sum for current columns
                col_sum = 0
                used_rows = set()
                for col in [i, k]:
                    for j in range(m):
                        if j not in used_rows:
                            col_sum += board[j][col]
                            used_rows.add(j)
                            break
                # Find remaining max value
                remaining_max = max([r for j, r in enumerate(row_max) if j not in used_rows])
                max_sum = max(max_sum, col_sum + remaining_max)
        
        return max_sum
