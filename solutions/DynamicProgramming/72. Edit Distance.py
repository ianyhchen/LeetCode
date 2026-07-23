class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # 1. 宣告 m + 1 列 (word1), n + 1 欄 (word2)
        # 內層是 n + 1 (欄)，外層跑 m + 1 次 (列)
        dp = [[0]*(n + 1) for _ in range(m + 1)]

        # 2. 初始化第一列 (i = 0, word1 為空，轉換成 word2 需要 j 次插入)
        for j in range(n + 1):
            dp[0][j] = j

        # 3. 初始化第一欄 (j = 0, word2 為空，word1 轉換過去需要 i 次刪除)
        for i in range(m + 1):
            dp[i][0] = i 

        # 4. 進行狀態轉移
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j - 1],   #Replace
                        dp[i - 1][j],       # Delete
                        dp[i][j - 1]        # Insert
                        ) + 1

        return dp[m][n]