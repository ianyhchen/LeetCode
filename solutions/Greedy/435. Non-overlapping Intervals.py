# 為了讓後面能留出更多的空間給其他區間，我們應該優先選擇最早結束的區間
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by end time first, then by start time
        # This ensures we always pick the interval that finishes earliest
        intervals.sort(key=lambda x: (x[1], x[0]))

        # Initialize current_end to negative infinity to handle negative intervals
        current_end = float('-inf')
        erase_count = 0
        for start, end in intervals:
            # If the current interval's start is greater than or equal to 
            # the last kept interval's end, there is no overlap
            if start >= current_end:
                # Update current_end to the current interval's end
                current_end = end
            else:
                # Overlap detected, increment the count of intervals to be removed
                erase_count += 1

        return erase_count
