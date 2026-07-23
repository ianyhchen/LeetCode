from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Stores indices of elements, keeping the values in monotonic decreasing order
        queue = deque()
        result = []
        
        for i in range(len(nums)):
            # Maintain monotonic property: remove indices of smaller elements from the back
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            
            # Add the current element's index to the back of the queue
            queue.append(i)

            # Remove the index from the front if it is out of the current window's bound
            if queue[0] < i - k + 1:
                queue.popleft()
            
            # Append the maximum element of the current window to the result
            # The window is fully formed when the index 'i' reaches at least k - 1
            if i >= k - 1:
                result.append(nums[queue[0]])                
        
        return result