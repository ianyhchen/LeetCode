import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        prefixGcd = []
        current_max = 0
        
        for num in nums:
            current_max = max(current_max, num)
            prefixGcd.append(math.gcd(num, current_max))
        
        prefixGcd.sort()
        
        left, right = 0, n - 1
        sum = 0

        while left < right:
            sum += gcd(prefixGcd[left], prefixGcd[right])

            left += 1
            right -= 1
        
        return sum 