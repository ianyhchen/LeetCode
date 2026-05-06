class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Edge case: if matrix is empty, return 0
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        # Initialize (rows + 1) x (cols + 1) DP table with zeros
        # Padding helps handle boundary conditions (first row/column) automatically
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        max_side_len = 0

        # Iterate through the DP table starting from index (1, 1)
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                # If current cell in original matrix is '1'
                # Note: dp[i][j] corresponds to matrix[i-1][j-1]
                if matrix[i - 1][j - 1] == '1':
                    # The current side length depends on the minimum of 
                    # its Top, Left, and Top-Left neighbors
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

                    # Update the global maximum side length found so far
                    max_side_len = max(max_side_len, dp[i][j])
                    
        # The result is the area of the square, which is side length squared
        return max_side_len * max_side_len
