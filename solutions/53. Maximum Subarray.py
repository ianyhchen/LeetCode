#Dynamic programming
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #maxSum 初始化不能為0, 因為可能全部都是負數
        maxSum = currentSum = nums[0]
                
        #從第二個數字開始
        for num in nums[1:]:
            #若加上currentSum後反而變小，直接從目前數字重新開始計算
            currentSum = max(num, currentSum + num)            
            maxSum = max(maxSum, currentSum)
        return maxSum
    
# Divide and conquer solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       return self.solve(nums, 0, len(nums) - 1)

    def solve(self, nums: List[int], left: int, right: int) -> int:
        # Base case: when only has one element, the max sum is itself
        if left == right:
            return nums[left]
        
        # Divide: find the mid
        mid = (left + right) // 2

        # Conquer: 遞迴計算左半部與右半部的最大子陣列和
        left_sum = self.solve(nums, left, mid)
        right_sum = self.solve(nums, mid + 1, right)

        # Combine: 計算「跨越中點」的最大子陣列和
        cross_sum = self.max_cross_sum(nums, left, mid, right)

        return max(left_sum, right_sum, cross_sum)

    def max_cross_sum(self, nums: List[int], left: int, mid: int, right: int) -> int:
        # 從 mid 開始向左掃描，找最大累積和
        left_max = -float('inf')
        current_sum = 0
        for i in range(mid, left - 1, -1):
            current_sum += nums[i]
            left_max = max(left_max, current_sum)
        
        # 從 mid + 1 開始向右掃描，找最大累積和
        right_max = -float('inf')
        current_sum = 0
        for i in range(mid + 1, right + 1):
            current_sum += nums[i]
            right_max = max(right_max, current_sum)

        # 跨越中點的最大和 = 左側貢獻 + 右側貢獻
        return left_max + right_max