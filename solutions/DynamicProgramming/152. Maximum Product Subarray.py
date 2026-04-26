'''
動態規劃 (DP) - 維護正負兩極
因為負負得正，我們不能只記錄到目前為止的最大乘積，還必須記錄最小乘積（負得最多的那個）
複雜度：時間 O(n)，空間 O(1)
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0    

        # Initialize with the first element
        res = nums[0]
        current_max, current_min = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]

            # If current number is negative, swap max and min
            if nums[i] < 0:
                current_max, current_min = current_min, current_max
            
            # Update max and min: 
            # Either start a new subarray at current num, or extend previous
            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)

            # Record the highest product seen so far
            res = max(res, current_max)            
                   
        return res