from collections import Counter
from heapq import heappush, heappop
class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counter = Counter(s)
        max_count = 0
        max_heap = []
        for key, value in counter.items():
            max_count = max(max_count, value)
            heappush(max_heap, (-value, key))

        # Pigeonhole principle check
        if max_count > (n + 1) // 2:
            return ""
        
        result = []
        prev = None
        while max_heap:
            curr_value, curr_char = heappop(max_heap)

            result.append(curr_char)
            curr_value += 1 # Decrement the actual frequency (since it's negative)

            # If there was a previously deferred character, push it back to heap
            if prev and prev[0] < 0:
                heappush(max_heap, prev)
                
            # Defer the current character for the next iteration
            prev = (curr_value, curr_char)
        
        return ''.join(result)