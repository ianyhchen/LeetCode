#Simulation, time complexity:O(n**2)
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        for right in range(n - 1, 0, -1):
            for i in range(right):
                nums[i] = (nums[i] + nums[i + 1]) % 10
        
        return nums[0]
        