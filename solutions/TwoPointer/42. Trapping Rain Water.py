'''
對於任何一個位置 i，它能接多少水，取決於它 左邊最高的柱子 和 右邊最高的柱子
- 公式：water[i] = min(left_max, right_max) - height[i]
- 只有當 min(left_max, right_max) > height[i] 時，該位置才能存水。

Two pointer: 利用左右指針往中間靠攏，誰短就處理誰，因為短的那邊才是決定水位的關鍵。
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        left, right = 0, n - 1
        left_max, right_max = 0, 0 
        total_water = 0

        while left < right:
            # Decide which pointer to move based on the lower wall
            if height[left] < height[right]:
                # Process the left side
                if height[left] >= left_max:
                    # Update the maximum height encountered from the left                
                    left_max = height[left]
                else:
                    # Water trapped is the difference between max wall and current height
                    total_water += left_max - height[left]                
                left += 1
            else:
                # Process the right side
                if height[right] >= right_max:
                    # Update the maximum height encountered from the right
                    right_max = height[right]
                else:
                    # Water trapped is the difference between max wall and current height
                    total_water += right_max - height[right]
                right -= 1
        
        return total_water
