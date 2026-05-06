#輸入特性：每個元素 `nums[i]` 代表在該位置能跳躍的「最大長度」，而非固定步數。
#關鍵邏輯：只要能到達 index `i`，則所有小於 `i` 的位置必然都能到達。
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # max_reach tracks the furthest index we can currently reach
        max_reach = 0
        n = len(nums)
        for i in range(n):
            # If the current index is greater than max_reach, 
            # it means this position is unreachable.
            if i >  max_reach:
                return False

            # Update max_reach by comparing the current max_reach 
            # with the furthest possible jump from the current index (i + nums[i]).
            max_reach = max(max_reach, i + nums[i])

            # Early exit optimization: if we can already reach or surpass 
            # the last index, return True immediately.
            if max_reach >= n - 1:
                return True
            
        # This line is technically a fallback, as the logic above 
        # covers all cases for valid or invalid paths.
        return max_reach >= n - 1