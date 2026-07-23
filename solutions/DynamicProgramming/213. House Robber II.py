'''
定義 dp[i] 為考慮前 i 間房屋時能搶到的最大金額
轉移方程：
對第 i 間房屋，你可以選擇：
    - 不搶：最大金額為 dp[i-1]。
   -  搶：最大金額為 dp[i-2] + nums[i]。
dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

破解「環狀結構」的核心思路：拆解成兩個線性問題
搶了第一間，就不可能搶最後一間:考慮範圍：nums[0] 到 nums[n-2]。
搶了最後一間，就不可能搶第一間:考慮範圍：nums[1] 到 nums[n-1]。
兩間都不搶: 考慮範圍包含在上述兩種情況中。
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        n = len(nums)
        if n == 1:
            return nums[0]
        def rob_helper(num_list: List[int]):
            n = len(num_list)
            if n == 1 :
                return num_list[0]
            dp = [0] * n
            dp[0] = num_list[0]
            dp[1] = max(num_list[0], num_list[1])
            
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + num_list[i])                    
            return dp[-1]
        
        return max(rob_helper(nums[:-1]), rob_helper(nums[1:]))
    
# 兩個參數，空間優化版本
class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        n = len(nums)
        if n == 1:
            return nums[0]
        def rob_helper(num_list: List[int]):    
            prev, curr = 0, 0
            
            for num in num_list:
                prev, curr = curr, max(curr, prev + num)                    
            return curr
        
        return max(rob_helper(nums[:-1]), rob_helper(nums[1:]))