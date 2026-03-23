class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort by start time
        intervals.sort(key=lambda x: x[0])
        merged = []

        for start, end in intervals:
            # if merged is empty or current interval is not overlapped with last element in the list
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                # overlapped                
                merged[-1][1] = max(merged[-1][1], end)
        
        return merged

        