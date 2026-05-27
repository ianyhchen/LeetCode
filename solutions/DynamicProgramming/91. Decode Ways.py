class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            # 檢查個位數 s[i-1]
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]

            # 檢查雙位數 s[i-2:i]
            two_digit = int(s[i - 2 : i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]  # 這裡 i=2 時，就會抓到 dp[0]
            
            if dp[i] == '0':
                return 0

        return dp[n]
