class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i-1], dp[i - 2] + nums[i])
        # Boundary case: if there's only one house, rob it
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # dp[i] stores the maximum money that can be robbed from the first i houses
        dp = [0] * len(nums)

        # Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # State transition: 
        # Option 1: Don't rob current house, take the max from the previous house (dp[i-1])
        # Option 2: Rob current house, take current money + max from two houses ago (nums[i] + dp[i-2])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i - 2] + nums[i])
        
        return dp[-1]
    
# 空間優化版本
class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i-1], dp[i - 2] + nums[i])
        # Boundary case: if there's only one house, rob it
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]        

        # Base cases
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        
    
        for i in range(2, len(nums)):
            # Python evaluates the entire right-hand side first, then assigns to the left            
            prev2, prev1 = prev1, max(prev1, prev2 + nums[i])
           
        
        return prev1