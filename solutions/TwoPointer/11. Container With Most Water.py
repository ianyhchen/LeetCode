class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n <= 1:
            return 0     
        left, right = 0, n - 1
        # Area = min(height[i], height[j]) * (j - i)
        max_area = 0
        while left < right:
            area = min(height[right], height[left]) * (right - left)
            max_area = max(max_area, area)

            if height[right] <= height[left]:
                right -= 1
            else:
                left += 1
        
        return max_area
