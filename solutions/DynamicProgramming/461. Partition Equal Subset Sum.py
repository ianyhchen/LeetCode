'''
DP problem

二維
X X X X i
dp[i][s]: from first i elements, if there is a method to pick some numbers whose sum equals to s

I. 不選i dp[i - 1][s] == true => dp[i][s] = true
II. 選i  dp[i - 1][s - nums[i]] == true => dp[i][s] = true

dp[i][s] = dp[i - 1][s] || (s >= nums[i] && dp[i - 1][s - nums[i]])

一維
dp[i] => 目前我們是否能湊出總和為 i 的子集
dp[i] =  dp[i] or dp[i - num]
'''


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        n = len(nums)
        
        # dp[i][j] means: using the first 'i' numbers, can we form a sum of 'j'?
        # Rows: 0 to n (using i numbers)
        # Cols: 0 to target (sum value)
        dp= [[False]* (target + 1) for _ in range(n + 1)]

        # Base case: A sum of 0 is always possible (by picking an empty subset)
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            current_num = nums[i - 1] # Note: nums is 0-indexed, so we use i-1
            for j in range(1, target + 1):
                # Case 1: Current number is too big, cannot pick it
                # Inherit the result from not using this number (the row above)
                if j < current_num:
                    dp[i][j] = dp[i - 1][j]
                else:
                    # Case 2: We have a choice
                    # - Don't pick current_num: dp[i-1][j]
                    # - Pick current_num: dp[i-1][j - current_num]
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - current_num]
            
            # Optimization: If we found a way to reach target, we can stop early
            if dp[i][target]:
                return True
        return dp[n][target]