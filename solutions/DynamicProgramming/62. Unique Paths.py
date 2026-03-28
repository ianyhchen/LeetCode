#DP 一維 solution
# O(m * n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # First row: only move right is acceptable => dp[0][j] = 1
        # First col: only down is accptable => dp[i][0] = 1
        # Start point: dp[0][0] = 1

        dp = [[1] * n for _ in range(m) ]

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        
        return dp[m - 1][n - 1]

#DP 二維 solution
# 不太好懂
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 1D array representing one row
        # All values are 1 because there's only 1 way to reach any cell in the first row
        dp = [1] * n

        # We start from the second row (index 1) because the first row is already [1, 1, ..., 1]
        for r in range(1, m):           
            # We start from the second column (index 1) because the first column 
            # of any row is always 1 (can only come from the cell above)
            for c in range(1, n):
                # Standard DP: dp[c] (new) = dp[c] (above/old) + dp[c-1] (left/new)
                dp[c] = dp[c] + dp[c - 1]

        # The last element is our destination (m-1, n-1)
        return dp[n - 1]


# Recursion(DFS) and memorization
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dfs(r, c) = dfs(r - 1, c) + dfs(r, c - 1)
        # 1. Create a memo (dictionary)
        memo = {}
        def dfs(r, c):
            # 2. Base Cases
            if r == 0 or c == 0:
                return 1
            elif r < 0 or c < 0:
                return 0

            # 3. Check if we already calculated this cell
            if (r, c)  in memo:
                return memo[(r, c)]

            # 4. Calculate, STORE in memo, and then return
            # This is the "Magic" part
            memo[(r, c)] = dfs(r - 1, c) + dfs(r, c - 1)

            return memo[(r, c)] 

        return dfs(m - 1, n - 1)