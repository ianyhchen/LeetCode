'''
1. 順序問題：
這題要求的是「排列」。在寫 DP 時，如果你的外層迴圈遍歷 target，內層遍歷 nums，你得到的是排列數（即本題要求）。
如果你外層遍歷 nums，內層遍歷 target，你得到的會是組合數（即 Coin Change II 的解法）

為什麼這題不適合用 Backtracking？
雖然 Backtracking 可以找到具體的組合路徑，但這題只要求「個數」。
由於 target 可能較大且數字可以重複使用，搜尋空間會呈指數級成長，單純的暴力搜尋會非常緩慢。
'''


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
            
        return dp[target]