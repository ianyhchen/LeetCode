from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x, y in points:
            # Calculate squared distance to avoid sqrt() overhead
            dist = x**2 + y**2

            # Python's heapq is a min-heap, so we push negative distances 
            # to simulate max-heap behavior.
            heappush(max_heap, (-dist, [x, y]))

            # If the heap size exceeds k, pop the element with the 
            # "largest" negative distance (which is the actual smallest value in min-heap)
            if len(max_heap) > k:
                heappop(max_heap)
        
        return [item[1] for item in max_heap]
    
'''
time complexity: O(N log k)
'''