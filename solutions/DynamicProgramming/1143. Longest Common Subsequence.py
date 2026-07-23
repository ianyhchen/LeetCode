class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] represents the length of LCS of text1[0 ... i-1] and text2[0 ... j-1]
        # Size is (m + 1) x (n + 1) to accommodate the base cases (empty strings)
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Iterate through both strings
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If characters match, extend the LCS from the top-left diagonal
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # If characters do not match, take the maximum LCS by either omitting
                    # text1[i-1] (top) or text2[j-1] (left)
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # The bottom-right cell contains the LCS length for full text1 and text2
        return dp[m][n]